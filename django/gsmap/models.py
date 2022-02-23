import json
import os
import secrets
import string
import hashlib
import requests
from enum import IntFlag
import bleach

from sortedm2m.fields import SortedManyToManyField
from sorl.thumbnail import ImageField, get_thumbnail

from django.db import transaction, DatabaseError
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.gis.db import models
from django.contrib.postgres import fields as pg_fields
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.utils.html import escape, format_html
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.sites.models import Site


from parler.models import TranslatableModel, TranslatedFields

from django.contrib.auth.models import Group
from gsuser.models import User
from main.utils import get_website

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or os.getenv('DJANGO_SECRET_KEY_DEV')

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


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

    @property
    def bfs_number(self):
        return self.id

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
        default=SnapshotPermission.NOT_LISTED
    )

    title = models.CharField(max_length=150, default='')
    topic = models.CharField(max_length=100, default='')
    data = models.JSONField(default=dict)
    data_file = models.FileField(upload_to='data-files', null=True, blank=True)
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

    def __str__(self):
        if self.municipality:
            return f'{self.municipality.fullname}, {self.title},' \
                f'{self.id}, {self.user}, ({self.get_permission_display()})'
        else:
            return self.title

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
        return self.screenshot_manual or self.screenshot_generated or None

    @property
    def thumbnail(self):
        return self.thumbnail_manual or self.thumbnail_generated or None

    @property
    def data_file_dict(self):
        if self.data_file:
            self.data_file.open()
            data = self.data_file.read()
            return data
        return str(dict())

    @property
    def data_file_json(self):
        return json.loads(self.data_file_dict)

    @property
    def title_data(self):
        try:
            data = self.data_file_json
            return data['views'][0]['spec']['title']
        except KeyError:
            return self.title

    @property
    def description_data(self):
        try:
            data = self.data_file_json
            data = data['views'][0]['spec']['description']
            return (data[:75] + '…') if len(data) > 75 else data
        except KeyError:
            return ''

    def get_absolute_link(self):
        website = get_website(Site.objects.get_current())
        return format_html(
            f'<a href="{website["proto"]}://{website["domain"]}{self.get_absolute_url()}" target="_blank">'
            f'{website["domain"]}{self.get_absolute_url()}</a>'
        )
    get_absolute_link.short_description = "Snapshot Url"

    def get_absolute_url(self):
        return f'/{self.id}/'

    def image_twitter(self):
        if bool(self.screenshot):
            return get_thumbnail(
                self.screenshot, '1200x600',
                crop='bottom', format='PNG'
            )
        return ''

    def image_facebook(self):
        if bool(self.screenshot):
            return get_thumbnail(
                self.screenshot, '1200x630',
                crop='bottom', format='PNG'
            )

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

        if not self._state.adding:
            if bool(self.data_file):
                storage = OverwriteStorage()
                if self.permission is int(SnapshotPermission.PUBLIC):
                    self.create_meta(storage)
                else:
                    storage.delete(f'snapshot-meta/{self.id}.html')

        if not self._state.adding and bool(self.data_file):
            if self.data_changed(['data_file']):
                self.clean_screenshot()

        try:
            super().save(*args, **kwargs)
        except DatabaseError:
            transaction.rollback()

    def create_screenshot(self):
        # TODO check for resources key in json file
        # if not 'resources' in data:
        #     raise ValueError('no resources key in data')

        self.screenshot_generated = self.create_screenshot_file()
        self.thumbnail_generated = self.create_screenshot_file(is_thumbnail=True)
        self.save()

    def clean_screenshot(self):
        if self.screenshot_generated:
            self.screenshot_generated.delete()
        if self.thumbnail_generated:
            self.thumbnail_generated.delete()

    def create_screenshot_file(self, is_thumbnail=False):
        url = f'http://vue:8079/de/{self.pk}/?screenshot'
        path = 'snapshot-screenshots'
        if is_thumbnail:
            url += '&thumbnail'
            path = 'snapshot-thumbnails'
        response = requests.get(url, timeout=(100, 300))
        date_suffix = timezone.now().strftime("%Y-%m-%d_%H-%M-%SZ")
        screenshot_file = SimpleUploadedFile(
            f'{path}/{self.pk}_{date_suffix}.png',
            response.content, content_type="image/png"
        )
        return screenshot_file

    def create_meta(self, storage):
        website = get_website(Site.objects.get_current())
        meta = f'''
<meta property="og:title" content="{ escape(self.title_data) }">
<meta property="og:description" content="{ escape(self.description_data) }">
<meta property="og:type" content="website">
<meta property="og:url" content="{ website["proto"] }://{ website["domain"] }{ self.get_absolute_url() }">
<meta property="og:image" content="{ website["proto"] }://{ website["domain"] }/{ self.image_facebook() }">
<meta name="twitter:image" content="{ website["proto"] }://{ website["domain"] }/{ self.image_twitter() }">
'''
        storage.save(f'snapshot-meta/{self.id}.html', ContentFile(meta))


@receiver(post_save, sender=Snapshot)
def resave(sender, instance, created, **kwargs):
    """
    Triggers meta and image creations on an instance already
    in the database.
    """
    if created:
        transaction.on_commit(lambda: instance.save())

class Category(TranslatableModel):
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['namespace']

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    # my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    hide_in_list = models.BooleanField(default=False)

    namespace = models.CharField(max_length=255, default='core/beteiligung')
    icon = models.FileField(upload_to='category-icons', null=True, blank=True)
    color = models.CharField(max_length=7, default='#cccccc')

    translations = TranslatedFields(
        name=models.CharField(max_length=255),
    )
    # workspace =  models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.namespace}/{self.name}'

class Usergroup(TranslatableModel):
    class Meta:
        verbose_name_plural = 'usergroups'
        # ordering = ['name']

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    key = models.CharField(
        max_length=50, unique=True,
        primary_key=True
    )

    translations = TranslatedFields(
        name=models.CharField(max_length=255),
    )

    def __str__(self):
        return f'{self.name}'

class Workspace(models.Model):
    class Meta:
        ordering = ['-created']

    id = models.CharField(
        max_length=8, unique=True,
        primary_key=True, default=create_slug_hash_5
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    snapshots = SortedManyToManyField(Snapshot)

    categories = SortedManyToManyField(Category)
    usergroups = SortedManyToManyField(Usergroup)

    MODE_CHOICES = [
        ("OFF", _("Off")),
        ("MGT", _("Portfolio-/Flächenmanagement")),
        ("PAR", _("Beteiligung")),
    ]
    mode = models.CharField(max_length=3, choices=MODE_CHOICES, default="OFF")

    annotations_open = models.BooleanField(default=False, help_text="Enable marker annotations", verbose_name="Marker Annotations enabled")
    annotations_likes_enabled = models.BooleanField(default=True, help_text="Enable like buttons on marker annotations", verbose_name="Marker Likes enabled")

    polygon_open = models.BooleanField(default=False, help_text="Enable polygon annotation", verbose_name="Polygon annotations enabled")
    polygon_likes_enabled = models.BooleanField(default=False, help_text="Enable like buttons on polygon annotations", verbose_name="Polygon Likes enabled")

    annotations_contact_name = models.CharField(max_length=100, default='', verbose_name="Contact first & lastname")
    annotations_contact_email = models.EmailField(default='', verbose_name='Contact email address')

    findme_enabled = models.BooleanField(default=False, help_text="Enable 'Find Me'", verbose_name="Find me enabled")

    translations = TranslatedFields(
        title = models.CharField(max_length=150, default=''),
        description = models.TextField(default=''),
    )

    def get_absolute_link(self):
        website = get_website(Site.objects.get_current())
        return format_html(
            f'<a href="{website["proto"]}://{website["domain"]}{self.get_absolute_url()}" target="_blank">'
            f'{website["domain"]}{self.get_absolute_url()}</a>')

    get_absolute_link.short_description = "Workspace Url"

    def get_absolute_url(self):
        first_id = self.snapshots.all().first().id
        return f'/{self.id}/{first_id}/'

    def get_relative_url(self):
        return self.get_absolute_url()[1:-1]

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
        return f'{self.id}'

class Annotation(models.Model):
    class Meta:
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    KIND_CHOICES = [
        ('COM', 'Comment'),
        ('PLY', 'Polygon'),
    ]
    kind = models.CharField(max_length=3, choices=KIND_CHOICES)
    data = models.JSONField(default=dict)
    category = models.ForeignKey(
        Category, default=None, blank=True,
        null=True, on_delete=models.SET_NULL
    )
    usergroup = models.ForeignKey(
        Usergroup, default=None, blank=True,
        null=True, on_delete=models.SET_NULL
    )
    author_email = models.EmailField(max_length=254)
    rating = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.data['properties']['description']:
            self.data['properties']['description'] = bleach.clean(self.data['properties']['description'])

        if self.data['properties']['title']:
            self.data['properties']['title'] = bleach.clean(self.data['properties']['title'])
        
        super().save(*args, **kwargs)

    @property
    def fullname(self):
        return f'{self.workspace} {self.id} {self.data["properties"]["title"]}'
    
    @property
    def title(self):
        if "properties" in self.data.keys() and "title" in self.data["properties"].keys():
            return f'{self.data["properties"]["title"]}'
        else:
            return None
    
    @property
    def description(self):
        if "properties" in self.data.keys() and "description" in self.data["properties"].keys():
            return f'{self.data["properties"]["description"]}'
        else:
            return None
    
    def __str__(self):
        return self.fullname

class Attachement(models.Model):
    class Meta:
        ordering = ['my_order']

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    annotation =  models.ForeignKey(Annotation, on_delete=models.CASCADE)
    document = models.FileField(upload_to='annotation-attachements', null=True, blank=True)
    #kind = models.CharField(max_length=4)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

@receiver(post_save, sender=Annotation)
def send_new_annotation_email(sender, instance, created, **kwargs):

      if created:
        recipient = instance.author_email
        subject = 'Kommentar freischalten'
        message = 'Besten Dank für Ihren Kommentar!\n'

        website = get_website(Site.objects.get_current())

        if instance.workspace.annotations_open:
            idstr = str(instance.id)

            uniquestr = recipient + idstr + SECRET_KEY
            publishKeyHex = hashlib.md5(uniquestr.encode()).hexdigest()
            publish_url = reverse('annotation-publish', args=[idstr, publishKeyHex])

            message += 'Sie können ihn unter folgender URL freischalten:\n'
            message += f'{website["base"]}{publish_url}\n'
            message += '--' * 30
        else:
            message += "Leider ist die Beteiligung nun abgeschlossen.\n"
            message += f"Zur Karte mit allen öffentlichen Kommentaren: {website['base']}/de/{instance.workspace.pk}/{instance.workspace.snapshots.first().pk}/"
            message += '--' * 30

        send_mail(
            subject,
            message,
            None,
            [ recipient ],
            fail_silently=False,
        )
