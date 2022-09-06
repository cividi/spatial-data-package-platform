from django.contrib.gis import admin
from parler.admin import TranslatableStackedInline
from django.conf import settings
from django.utils.translation import gettext as _
from solo.admin import SingletonModelAdmin
from main.models import ContentSection, SiteConfiguration

class ContentSectionInline(TranslatableStackedInline):
    model = ContentSection

class SiteConfigAdminAdmin(SingletonModelAdmin):
    fieldsets = (
        (_('Meta'), {
            'fields': ('search_enabled', 'example_gallery_enabled')
        }),
        (_('Legacy Snippet'), {
            'fields': ('homepage_snippet',)
        }),
    )
    inlines = [ ContentSectionInline, ]

admin.site.register(SiteConfiguration, SiteConfigAdminAdmin)
admin.site.site_header = settings.ADMIN_NAME