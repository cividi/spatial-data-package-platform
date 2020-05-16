import secrets
import string
from enum import IntFlag
import requests
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.gis.db import models
from django.contrib.postgres import fields as pg_fields
from django.contrib.sites.models import Site
from django.utils.html import format_html
from django.conf import settings
from sortedm2m.fields import SortedManyToManyField
from sorl.thumbnail import ImageField
from gsuser.models import User


class Municipality(models.Model):
    class Meta:
        verbose_name_plural = 'municipalities'
        ordering = ['name']

    CANTONS_CHOICES = [
        ('GR', 'Graubünden'),
        ('GL', 'Glarus'),
        ('VD', 'Vaud'),
        ('VS', 'Valais'),
        ('BE', 'Bern'),
        ('TI', 'Ticino'),
        ('SZ', 'Schwyz'),
        ('UR', 'Uri'),
        ('SG', 'St. Gallen'),
        ('NE', 'Neuchâtel'),
        ('TG', 'Thurgau'),
        ('FR', 'Fribourg'),
        ('LU', 'Luzern'),
        ('NW', 'Nidwalden'),
        ('OW', 'Obwalden'),
        ('ZH', 'Zürich'),
        ('JU', 'Jura'),
        ('AI', 'Appenzell Innerrhoden'),
        ('AR', 'Appenzell Ausserrhoden'),
        ('SH', 'Schaffhausen'),
        ('ZG', 'Zug'),
        ('SO', 'Solothurn'),
        ('BS', 'Basel-Stadt'),
        ('AG', 'Aargau'),
        ('GE', 'Genève'),
        ('BL', 'Basel-Landschaft'),
    ]

    name = models.CharField(max_length=100)
    canton = models.CharField(max_length=2, choices=CANTONS_CHOICES)
    perimeter = models.MultiPolygonField(null=True)
    centerpoint = models.PointField(null=True)

    @property
    def fullname(self):
        return f'{self.name} ({self.canton})'

    def __str__(self):
        return self.fullname


def create_slug_hash(hash_length):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(hash_length))

def create_slug_hash_5():
    return create_slug_hash(5)

def create_slug_hash_6():
    return create_slug_hash(6)


class SnapshotPermission(IntFlag):
    PUBLIC = 0
    NOT_LISTED = 10


class Snapshot(models.Model):
    class Meta:
        ordering = ['-created']

    id = models.CharField(
        max_length=8, unique=True,
        primary_key=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    is_showcase = models.BooleanField(default=False)
    permission = models.IntegerField(
        choices=[(perm.value, perm.name)
                 for perm in SnapshotPermission],
        default=SnapshotPermission.PUBLIC
    )

    title = models.CharField(max_length=150, default='')
    topic = models.CharField(max_length=100, default='')
    data = pg_fields.JSONField(default=dict)
    screenshot_generated = ImageField(upload_to='snapshot-screenshots', null=True, blank=True)
    thumbnail_generated = ImageField(upload_to='snapshot-thumbnails', null=True, blank=True)
    screenshot_manual = ImageField(upload_to='snapshot-screenshots', null=True, blank=True)
    thumbnail_manual = ImageField(upload_to='snapshot-thumbnails', null=True, blank=True)
    predecessor = models.ForeignKey(
        'self', default=None, blank=True,
        null=True, on_delete=models.SET_NULL
    )
    municipality = models.ForeignKey(
        Municipality, default=None, blank=True,
        null=True, on_delete=models.SET_NULL
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance._state.adding = False
        instance._state.db = db
        instance._old_values = dict(zip(field_names, values))
        return instance

    def data_changed(self, fields):
        if hasattr(self, '_old_values'):
            if not self.pk or not self._old_values:
                return True

            changed_list = []
            for field in fields:
                if getattr(self, field) != self._old_values[field]:
                    changed_list.append(True)
                changed_list.append(False)
            return any(changed_list)
        return True

    @property
    def screenshot(self):
        return self.screenshot_manual or self.screenshot_generated

    @property
    def thumbnail(self):
        return self.thumbnail_manual or self.thumbnail_generated

    def get_absolute_link(self):
        domain = Site.objects.get_current().domain
        return format_html(
            f'<a href="//{domain}{self.get_absolute_url()}" target="_blank">'
            f'{domain}{self.get_absolute_url()}</a>'
        )
    get_absolute_link.short_description = "Snapshot Url"

    def get_absolute_url(self):
        return f'/{self.id}/'

    def create_screenshot_file(self, is_thumbnail=False):
        url = f'http://vue:8079/de/{self.pk}/?screenshot'
        path = 'snapshot-screenshots'
        if is_thumbnail:
            url += '&thumbnail'
            path = 'snapshot-thumbnails'
        response = requests.get(url, timeout=(10, 50))
        date_suffix = timezone.now().strftime("%Y-%m-%d_%H-%M-%SZ")
        screenshot_file = SimpleUploadedFile(
            f'{path}/{self.pk}_{date_suffix}.png',
            response.content, content_type="image/png"
        )
        return screenshot_file

    def save(self, *args, **kwargs):
        def test_exists(pk):
            if list(self.__class__.objects.filter(pk=pk)):
                new_id = create_slug_hash_6()
                test_exists(new_id)
            else:
                return pk

        if self._state.adding:
            self.id = create_slug_hash_6()
            self.id = test_exists(self.id)

        super().save(*args, **kwargs)

    def image_twitter(self):
        return get_thumbnail(
            self.screenshot, '1200x630',
            crop='bottom', format='PNG'
        )

    def image_facebook(self):
        return get_thumbnail(
            self.screenshot, '1200x630',
            crop='bottom', format='PNG'
        )

    def __str__(self):
        if self.municipality:
            return f'{self.municipality.fullname}, {self.title}, ' \
                f'{self.id} ({self.get_permission_display()})'
        else:
            return self.title


@receiver(post_save, sender=Snapshot)
def save_screenshot_handler(sender, **kwargs):
    def save_screenshot():
        post_save.disconnect(save_screenshot_handler, sender=Snapshot)
        instance = kwargs.get('instance')
        # only create snapshot if data changed
        if instance.data_changed([
                'data', 'screenshot_generated', 'thumbnail_generated'
        ]) or not bool(instance.thumbnail_generated):
            if not 'resources' in instance.data:
                return
            try:
                # disconnect to break save recursive loop
                post_save.disconnect(save_screenshot_handler, sender=Snapshot)
                screenshot_file = instance.create_screenshot_file()
                thumbnail_file = instance.create_screenshot_file(is_thumbnail=True)
                instance.screenshot_generated = screenshot_file
                instance.thumbnail_generated = thumbnail_file
                instance.save()
            finally:
                # always reconnect signal
                post_save.connect(save_screenshot_handler, sender=Snapshot)
    if hasattr(settings, 'SAVE_SCREENSHOT_ENABLED') and settings.SAVE_SCREENSHOT_ENABLED is True:
        save_screenshot()


class Workspace(models.Model):
    class Meta:
        ordering = ['-created']

    id = models.CharField(
        max_length=8, unique=True,
        primary_key=True, default=create_slug_hash_5
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=150, default='')
    description = models.TextField(default='')

    snapshots = SortedManyToManyField(Snapshot)

    def get_absolute_link(self):
        domain = Site.objects.get_current().domain
        return format_html(
            f'<a href="//{domain}{self.get_absolute_url()}" target="_blank">'
            f'{domain}{self.get_absolute_url()}</a>'
        )
    get_absolute_link.short_description = "Workspace Url"

    def get_absolute_url(self):
        first_id = self.snapshots.all().first().id
        return f'/{self.id}/{first_id}/'


    def save(self, *args, **kwargs):
        def test_exists(pk):
            if self.__class__.objects.filter(pk=pk):
                new_id = create_slug_hash_5()
                test_exists(new_id)
            else:
                return pk

        if self._state.adding:
            self.id = test_exists(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.title}'
