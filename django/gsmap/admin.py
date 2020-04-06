from django.contrib.gis import admin
from django.utils.translation import gettext as _
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from gsmap.models import Municipality, Snapshot, Workspace


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
    list_display = ('id', 'title', 'permission', 'created', 'modified')

    def get_queryset(self, request):
        return self.model.objects_raw.all()


class WorkspaceAdmin(admin.OSMGeoAdmin):

    list_display = ('id', 'title', 'created', 'modified')

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'snapshots':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
admin.site.register(Workspace, WorkspaceAdmin)
