from django.contrib import admin
from gsmap.models import Municipality


class MunicipalityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Municipality, MunicipalityAdmin)
