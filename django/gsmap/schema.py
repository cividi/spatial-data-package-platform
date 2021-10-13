# pylint: disable=no-member,unused-argument
import json
import graphene
from django.contrib.gis.db import models
from django.contrib.gis.db.models import Q
from django_filters import FilterSet
from graphql_relay import from_global_id
from graphene.types import generic
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from gsmap.models import Municipality, Snapshot, SnapshotPermission, Workspace, Annotation, Category, Attachement
from graphene_django.rest_framework.mutation import SerializerMutation


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
        fields = [
            'is_showcase', 'title', 'topic', 'data', 'datafile', 'municipality',
            'predecessor'
        ]
        filter_fields = [
            'municipality__id', 'municipality__canton', 'is_showcase'
        ]
        interfaces = [graphene.relay.Node]

    data = generic.GenericScalar(source='data_file_json')
    datafile = graphene.String()
    pk = graphene.String(source='id')
    thumbnail = graphene.String()
    screenshot = graphene.String()
    screenshot_facebook = graphene.String()
    screenshot_twitter = graphene.String()

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(Q_SNAPSHOT_WITH_NOT_LISTED)

    def resolve_screenshot(self, info):
        return self.screenshot

    def resolve_thumbnail(self, info):
        return self.thumbnail

    def resolve_screenshot_facebook(self, info):
        return self.image_facebook()

    def resolve_screenshot_twitter(self, info):
        return self.image_twitter()

    def resolve_datafile(self, info):
        return self.data_file if self.data_file else None


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
        return Snapshot.objects.filter(Q_SNAPSHOT_ONLY_PUBLIC
                                       & Q(municipality__id=self.pk))

    def resolve_perimeter_centroid(self, info):
        return self.perimeter.centroid

    def resolve_perimeter_bounds(self, info):
        return self.perimeter.extent

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        fields = [ 'name', 'icon','my_order','hide_in_list']
        filter_fields = {
            'hide_in_list': ['exact'],
        }
        interfaces = [graphene.relay.Node]

class AttachementNode(DjangoObjectType):
    class Meta:
        model = Attachement
        fields = [ 'document','my_order']
        interfaces = [graphene.relay.Node]

class AnnotationNode(DjangoObjectType):
    class Meta:
        model = Annotation
        fields = [ 'kind', 'author_email', 'data', 'rating']
        interfaces = [graphene.relay.Node]
    
    category = graphene.List(CategoryNode)
    attachements = graphene.List(AttachementNode)
    data = generic.GenericScalar(source='data')

    def resolve_category(self, info):
        return Category.objects.filter(Q(id=self.category.id))
    
    def resolve_attachements(self, info):
        return Attachement.objects.filter(Q(deleted=0) & Q(annotation=self.id))

class WorkspaceNode(DjangoObjectType):
    class Meta:
        model = Workspace
        fields = ['title', 'description', 'annotations_open']
        interfaces = [graphene.relay.Node]

    pk = graphene.String(source='id')
    snapshots = graphene.List(SnapshotNode)

    annotations = graphene.List(AnnotationNode)

    categories = graphene.List(CategoryNode)

    def resolve_snapshots(self, info):
        return self.snapshots.all()

    def resolve_annotations(self, info):
        return Annotation.objects.filter(Q(public=1) & Q(workspace=self.pk))
    
    def resolve_categories(self, info):
        return Category.objects.filter(Q(hide_in_list=0))

class SnapshotMutation(graphene.relay.ClientIDMutation):
    class Input:
        title = graphene.String()
        topic = graphene.String()
        wshash = graphene.String()
        bfsNumber = graphene.String()

    snapshot = graphene.Field(SnapshotNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, client_mutation_id=None, **data):
        if not info.context.user.is_authenticated:
            return SnapshotMutation(snapshot=None)
        municipality = Municipality.objects.get(pk=int(data['bfsNumber']))
        if client_mutation_id:
            snapshot = Snapshot.objects.get(pk=from_global_id(client_mutation_id)[1])
            snapshot.title = data['title']
            snapshot.topic = data['topic']
            snapshot.municipality = municipality
            snapshot.save()
        else:
            workspace = Workspace.objects.get(pk=from_global_id(data['wshash'])[1])
            snapshot = Snapshot(title=data['title'], topic=data['topic'])
            snapshot.user = info.context.user
            snapshot.municipality = municipality
            snapshot.save()
            workspace.snapshots.add(snapshot)
        return SnapshotMutation(snapshot=snapshot)


class Query(object):
    municipality = graphene.relay.Node.Field(MunicipalityNode)
    municipalities = DjangoFilterConnectionField(MunicipalityNode)

    snapshot = graphene.relay.Node.Field(SnapshotNode)
    snapshots = DjangoFilterConnectionField(
        SnapshotNode, filterset_class=SnapshotOnlyPublicFilter)

    workspace = graphene.relay.Node.Field(WorkspaceNode)


class Mutation(graphene.ObjectType):
    snapshotmutation = SnapshotMutation.Field()

