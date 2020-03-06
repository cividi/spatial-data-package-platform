import secrets
import string
# from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres import fields as pg_fields
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
    canton = models.CharField(
        max_length=2,
        choices=CANTONS_CHOICES
    )
    perimeter = models.PolygonField(null=True)
    centerpoint = models.PointField(null=True)

    @property
    def fullname(self):
        return f'{self.name} ({self.canton})'

    def __str__(self):
        return self.fullname


def create_slug_hash():
    alphabet = string.ascii_uppercase + string.digits
    hash_length = 6
    return ''.join(secrets.choice(alphabet) for i in range(hash_length))


class Snapshot(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(
        max_length=8, unique=True, primary_key=True,
        default=create_slug_hash
    )
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
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

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        def test_exists(pk):
            if self.__class__.objects.filter(pk=pk):
                new_id = create_slug_hash()
                test_exists(new_id)
            else:
                return pk

        if self._state.adding:
            self.id = test_exists(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id
