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
            'fields': ('created', 'id', 'archived', 'deleted')
        }),
        (_('Main'), {
            'fields':
            ('data', 'screenshot', 'municipality', 'predecessor', 'user'),
        }),
    )
    list_display = ('id', 'created')


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
