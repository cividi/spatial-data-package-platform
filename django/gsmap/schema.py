import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gsmap.models import Municipality


class MunicipalityNode(DjangoObjectType):
    class Meta:
        model = Municipality
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'canton': ['exact']
        }
        interfaces = (graphene.relay.Node, )

    bfs_number = graphene.Int(source='pk')


class Query(object):
    municipality = graphene.relay.Node.Field(MunicipalityNode)
    all_municipalities = DjangoFilterConnectionField(MunicipalityNode)
