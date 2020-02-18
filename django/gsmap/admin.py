from django.contrib import admin
from django.utils.translation import gettext as _
from gsmap.models import Municipality, Snapshot


class MunicipalityAdmin(admin.ModelAdmin):
    pass


class SnapshotAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
    )
    fieldsets = (
        (_('Meta'), {
            'fields': ('created', 'slug_hash', 'archived', 'deleted')
        }),
        (_('Main'), {
            'fields': ('data', 'screenshot', 'predecessor', 'user'),
        }),
    )


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
