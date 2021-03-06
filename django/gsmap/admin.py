from django.contrib.gis import admin
from django.contrib.postgres import fields
from django.utils.translation import gettext as _
from django_json_widget.widgets import JSONEditorWidget
from django.utils.html import mark_safe
from django.contrib import messages
from django.forms.widgets import Textarea
import requests
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from gsmap.models import Municipality, Snapshot, Workspace


class MunicipalityAdmin(admin.OSMGeoAdmin):
    readonly_fields = ('bfs_number',)
    fields = ('bfs_number', 'name', 'canton', 'perimeter')
    list_display = (
        'name',
        'bfs_number',
    )
    list_filter = ('canton',)
    search_fields = ('id', 'name', 'canton')

    def get_map_widget(self, db_field):
        return Textarea



class SnapshotAdmin(admin.OSMGeoAdmin):
    readonly_fields = ('id', 'created', 'modified', 'get_absolute_link',
                       'thumbnail_generated_image', 'screenshot_generated_image',
                       'thumbnail_manual_image', 'screenshot_manual_image')
    fieldsets = (
        (_('Meta'), {
            'fields': ('id', 'get_absolute_link', 'created', 'modified',
                       'is_showcase', 'archived', 'deleted', 'permission')
        }),
        (_('Main'), {
            'fields': ('title', 'topic', 'data_file',),
        }),
        (_('Screenshots autogenerated'), {
            'fields': ('thumbnail_generated', 'thumbnail_generated_image',
                       'screenshot_generated', 'screenshot_generated_image'),
        }),
        (_('Screenshots manual (overwrite)'), {
            'fields': ('thumbnail_manual', 'thumbnail_manual_image',
                       'screenshot_manual', 'screenshot_manual_image'),
        }),
        (_('Relations'), {
            'fields': ('municipality', 'predecessor', 'user'),
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

    list_display = ('id', 'thumbnail_list_image', 'title', 'municipality',
                    'permission', 'is_showcase', 'created', 'modified', 'user', 'data_file')
    list_filter = ('is_showcase', 'permission')
    search_fields = ['title', 'municipality__name', 'municipality__canton']

    def _image_display(self, obj, width=None, link=True):
        if hasattr(obj, 'url'):
            html = '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.url, width=width, height='auto'
            )
            if link:
                html = '<a href="{url}" target="_blank">{html}</a>'.format(url=obj.url, html=html)
            return mark_safe(html)
        else:
            return '-'

    def screenshot_generated_image(self, obj):
        return self._image_display(obj.screenshot_generated, width=300)

    def thumbnail_generated_image(self, obj):
        return self._image_display(obj.thumbnail_generated, width=200)

    def thumbnail_list_image(self, obj):
        if obj.thumbnail_generated or obj.thumbnail_manual:
            return self._image_display(
                obj.thumbnail_generated or obj.thumbnail_manual,
                width=50, link=False
            )
        else:
            return '-'

    thumbnail_list_image.short_description = 'thumbnail'

    def screenshot_manual_image(self, obj):
        return self._image_display(obj.screenshot_manual, width=300)

    def thumbnail_manual_image(self, obj):
        return self._image_display(obj.thumbnail_manual, width=200)


    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError) as e:
            messages.error(
                request,
                f"Couldn't create the screenshots, screenshot server problem. (ReadTimeout, ConnectionError) {repr(e)}"
            )
        except Exception as e:
            messages.error(
                request,
                f"Couldn't create the screenshots, screenshot server problem. (Other Error) {repr(e)}"
            )


class WorkspaceAdmin(admin.OSMGeoAdmin):
    readonly_fields = ('id', 'created', 'modified', 'get_absolute_link')
    fieldsets = (
        (_('Meta'), {
            'fields': (
                'id', 'get_absolute_link',
                'created', 'modified'
            )
        }),
        (_('Main'), {
            'fields': ('title', 'description', 'snapshots'),
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
