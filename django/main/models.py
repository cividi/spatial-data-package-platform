from django.utils.translation import gettext as _
from solo.models import SingletonModel
from django.contrib.gis.db import models
from sorl.thumbnail import ImageField

from parler.models import TranslatableModel, TranslatedFields
from markdownx.models import MarkdownxField


class SiteConfiguration(SingletonModel):
    search_enabled = models.BooleanField(default=True)
    example_gallery_enabled = models.BooleanField(default=True)
    homepage_snippet = models.TextField(blank=True)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


class ContentSection(TranslatableModel, models.Model):
    siteConfiguration = models.ForeignKey(SiteConfiguration, on_delete=models.CASCADE)

    is_hero = models.BooleanField(default=False)
    
    translations = TranslatedFields(
        content = MarkdownxField(_('Markdown'), blank=True),
        image = ImageField(blank=True, null=True, upload_to='assets')
    )

    def __str__(self):
        if self.is_hero:
            return "Hero"
        if self.content:
            firstLine = self.content[0:self.content.find("\n")]
            return firstLine[0:100]
        return None
