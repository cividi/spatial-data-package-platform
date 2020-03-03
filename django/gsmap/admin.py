from django.contrib.gis import admin
from django.utils.translation import gettext as _
from gsmap.models import Municipality, Snapshot


class MunicipalityAdmin(admin.OSMGeoAdmin):
    pass


class SnapshotAdmin(admin.OSMGeoAdmin):
    readonly_fields = (
        'id', 'created',
    )
    fieldsets = (
        (_('Meta'), {
            'fields': ('created', 'id', 'archived', 'deleted')
        }),
        (_('Main'), {
            'fields':
            ('title', 'topic', 'data', 'screenshot'),
        }),
        (_('Relations'), {
            'fields':
            ('municipality', 'predecessor', 'user'),
        }),
        # (_('geo'), {
        #     'fields':
        #     ('perimeter',),
        # }),
    )
    list_display = ('id', 'created')


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
