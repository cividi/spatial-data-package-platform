# pylint: disable=no-member,unused-argument
import json
import graphene
from django.contrib.gis.db import models
from graphene.types import generic
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
# from sorl.thumbnail import get_thumbnail
from gsmap.models import Municipality, Snapshot


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


class SnapshotNode(DjangoObjectType):
    class Meta:
        model = Snapshot
        fields = ['is_showcase', 'title', 'topic', 'data', 'screenshot', 'municipality']
        filter_fields = ['municipality__id', 'municipality__canton', 'is_showcase']
        interfaces = [graphene.relay.Node]

    data = generic.GenericScalar(source='data')
    screenshot = graphene.Field(ImageNode)
    pk = graphene.String(source='id')


class MunicipalityNode(DjangoObjectType):
    class Meta:
        model = Municipality
        fields = ['name', 'canton', 'centerpoint']
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'canton': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = [graphene.relay.Node]

    bfs_number = graphene.Int(source='pk')
    fullname = graphene.String(source='fullname')
    snapshots = graphene.List(SnapshotNode)

    def resolve_snapshots(self, info):
        return Snapshot.objects.filter(municipality__id=self.pk)


class Query(object):
    municipality = graphene.relay.Node.Field(MunicipalityNode)
    municipalities = DjangoFilterConnectionField(MunicipalityNode)

    snapshot = graphene.relay.Node.Field(SnapshotNode)
    snapshots = DjangoFilterConnectionField(SnapshotNode)
