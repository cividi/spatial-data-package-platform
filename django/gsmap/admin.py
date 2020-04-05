from django.contrib.gis import admin
from django.utils.translation import gettext as _
from gsmap.models import Municipality, Snapshot


class MunicipalityAdmin(admin.OSMGeoAdmin):
    pass


class SnapshotAdmin(admin.OSMGeoAdmin):
    readonly_fields = (
        'id', 'created', 'modified'
    )
    fieldsets = (
        (_('Meta'), {
            'fields': (
                'id', 'created', 'modified', 'is_showcase', 'archived', 'deleted', 'permission'
            )
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

    def get_queryset(self, request):
        return self.model.objects_raw.all()


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
