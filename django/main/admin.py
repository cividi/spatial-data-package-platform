from django.contrib.gis import admin
from django.conf import settings
from solo.admin import SingletonModelAdmin
from main.models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.site_header = settings.ADMIN_NAME
