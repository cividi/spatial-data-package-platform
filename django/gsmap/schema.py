# pylint: disable=no-member,unused-argument
import json
import graphene
from django.contrib.gis.db import models
from django.contrib.gis.db.models import Q
from django_filters import FilterSet
from graphene.types import generic
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
# from sorl.thumbnail import get_thumbnail
from gsmap.models import Municipality, Snapshot, SnapshotPermission, Workspace


class GeoJSON(graphene.Scalar):
    @classmethod
    def serialize(cls, value):
        return json.loads(value.geojson)


@convert_django_field.register(models.GeometryField)
def convert_field_to_geojson(field, registry=None):
    return graphene.Field(
        GeoJSON,
        description=field.help_text,
        required=not field.null
    )


class ThumbnailNode(graphene.ObjectType):
    url = graphene.String()
    size = graphene.String()


class ImageNode(graphene.ObjectType):
    url = graphene.String()
    thumbnail = graphene.Field(ThumbnailNode, size=graphene.String())

    def resolve_url(self, info):
        return self.url

    def resolve_thumbnail(self, info, size):
        return ThumbnailNode(self, size=size)


Q_SNAPSHOT_ONLY_PUBLIC = Q(permission__exact=SnapshotPermission.PUBLIC)
Q_SNAPSHOT_WITH_NOT_LISTED = Q(permission__lte=SnapshotPermission.NOT_LISTED)


class SnapshotOnlyPublicFilter(FilterSet):
    class Meta:
        model = Snapshot
        fields = ['municipality__id', 'municipality__canton', 'is_showcase']

    @property
    def qs(self):
        return super().qs.filter(Q_SNAPSHOT_ONLY_PUBLIC)


class SnapshotNode(DjangoObjectType):
    class Meta:
        model = Snapshot
        fields = ['is_showcase', 'title', 'topic', 'data', 'screenshot', 'municipality']
        filter_fields = ['municipality__id', 'municipality__canton', 'is_showcase']
        interfaces = [graphene.relay.Node]

    data = generic.GenericScalar(source='data')
    screenshot = graphene.Field(ImageNode)
    pk = graphene.String(source='id')

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(Q_SNAPSHOT_WITH_NOT_LISTED)


class MunicipalityNode(DjangoObjectType):
    class Meta:
        model = Municipality
        fields = ['name', 'canton', 'centerpoint', 'perimeter']
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'canton': ['exact', 'icontains'],
        }
        interfaces = [graphene.relay.Node]

    bfs_number = graphene.Int(source='pk')
    fullname = graphene.String(source='fullname')
    snapshots = graphene.List(SnapshotNode)
    perimeter_centroid = GeoJSON()
    perimeter_bounds = graphene.List(graphene.Float)

    def resolve_snapshots(self, info):
        return Snapshot.objects.filter(Q_SNAPSHOT_ONLY_PUBLIC & Q(municipality__id=self.pk))

    def resolve_perimeter_centroid(self, info):
        return self.perimeter.centroid

    def resolve_perimeter_bounds(self, info):
        return self.perimeter.extent


class WorkspaceNode(DjangoObjectType):
    class Meta:
        model = Workspace
        fields = [
            'title', 'description'
        ]
        interfaces = [graphene.relay.Node]

    pk = graphene.String(source='id')
    snapshots = graphene.List(SnapshotNode)

    def resolve_snapshots(self, info):
        return self.snapshots.all()


class Query(object):
    municipality = graphene.relay.Node.Field(MunicipalityNode)
    municipalities = DjangoFilterConnectionField(MunicipalityNode)

    snapshot = graphene.relay.Node.Field(SnapshotNode)
    snapshots = DjangoFilterConnectionField(
        SnapshotNode, filterset_class=SnapshotOnlyPublicFilter
    )

    workspace = graphene.relay.Node.Field(WorkspaceNode)
