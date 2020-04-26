import secrets
import string
from enum import IntFlag
from django.contrib.gis.db import models
from django.contrib.postgres import fields as pg_fields
from django.contrib.sites.models import Site
from django.utils.html import format_html
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
        primary_key=True, default=create_slug_hash_6
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    is_showcase = models.BooleanField(default=False)
    permission = models.IntegerField(choices=[(perm.value, perm.name)
                                              for perm in SnapshotPermission],
                                     default=SnapshotPermission.PUBLIC)

    title = models.CharField(max_length=150, default='')
    topic = models.CharField(max_length=100, default='')
    data = pg_fields.JSONField(default=dict)
    screenshot = ImageField(upload_to='snapshot-screenshots')
    predecessor = models.ForeignKey(
        'self', default=None, blank=True,
        null=True, on_delete=models.SET_NULL
    )
    municipality = models.ForeignKey(
        Municipality, default=None, blank=True,
        null=True, on_delete=models.SET_NULL
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_link(self):
        domain = Site.objects.get_current().domain
        return format_html(
            f'<a href="//{domain}{self.get_absolute_url()}" target="_blank">'
            f'{domain}{self.get_absolute_url()}</a>'
        )
    get_absolute_link.short_description = "Snapshot Url"

    def get_absolute_url(self):
        return f'/{self.id}/'

    def save(self, *args, **kwargs):
        def test_exists(pk):
            if self.__class__.objects.filter(pk=pk):
                new_id = create_slug_hash_6()
                test_exists(new_id)
            else:
                return pk

        if self._state.adding:
            self.id = test_exists(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.municipality.fullname}, {self.title}, ' \
               f'{self.id} ({self.get_permission_display()})'


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
