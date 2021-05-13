from solo.models import SingletonModel
from django.contrib.gis.db import models

class SiteConfiguration(SingletonModel):
    search_enabled = models.BooleanField(default=True)
    example_gallery_enabled = models.BooleanField(default=True)
    homepage_snippet = models.TextField(blank=True)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
