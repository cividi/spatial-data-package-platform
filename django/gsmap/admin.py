from django.contrib import admin
from gsmap.models import Municipality, Snapshot


class MunicipalityAdmin(admin.ModelAdmin):
    pass


class SnapshotAdmin(admin.ModelAdmin):
    pass


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
