import graphene
import gsmap.schema
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from main.models import SiteConfiguration


class SiteConfigurationNode(DjangoObjectType):
    class Meta:
        model = SiteConfiguration
        filter_fields = ['id']
        fields = ['id', 'pk', 'search_enabled', 'homepage_snippet']
        interfaces = [graphene.relay.Node]
    
    pk = graphene.String(source='id')


class Query(gsmap.schema.Query, graphene.ObjectType):
    config = DjangoFilterConnectionField(SiteConfigurationNode)


class Mutation(gsmap.schema.Mutation, graphene.ObjectType):
    pass

# pylint: disable=invalid-name
schema = graphene.Schema(query=Query, mutation=Mutation)
