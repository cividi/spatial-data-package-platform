from django.contrib.gis import admin
from django.contrib.postgres import fields
from django.utils.translation import gettext as _
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from django_json_widget.widgets import JSONEditorWidget
from gsmap.models import Municipality, Snapshot, Workspace


class MunicipalityAdmin(admin.OSMGeoAdmin):
    pass


class SnapshotAdmin(admin.OSMGeoAdmin):
    readonly_fields = ('id', 'created', 'modified', 'get_absolute_link')
    fieldsets = (
        (_('Meta'), {
            'fields': (
                'id', 'get_absolute_link', 'created', 'modified', 'is_showcase', 'archived', 'deleted', 'permission'
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

    formfield_overrides = {
        fields.JSONField: {
            'widget': JSONEditorWidget
        },
    }

    list_display = ('id', 'title', 'municipality', 'permission', 'is_showcase',
                    'created', 'modified')
    list_filter = ('is_showcase', 'permission')
    search_fields = ['title', 'municipality__name', 'municipality__canton']


class WorkspaceAdmin(admin.OSMGeoAdmin):
    readonly_fields = ('id', 'created', 'modified')
    fieldsets = (
        (_('Meta'), {
            'fields': (
                'id', 'created', 'modified'
            )
        }),
        (_('Main'), {
            'fields':
            ('title', 'description', 'snapshots'),
        }),
    )
    list_display = ('id', 'title', 'created', 'modified')
    search_fields = ['title']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'snapshots':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
admin.site.register(Workspace, WorkspaceAdmin)
