import graphene
import gsmap.schema
from bs4 import BeautifulSoup
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from main.models import SiteConfiguration

class SiteConfigurationNode(DjangoObjectType):
    class Meta:
        model = SiteConfiguration
        fields = ['id', 'search_enabled', 'homepage_snippet']

    def resolve_homepage_snippet(self, info):
        language = self.language
        soup = BeautifulSoup(self.homepage_snippet, features='html.parser')
        if language:
            found = soup.find(lang=language)
            if found:
                return found
        return soup.div

class Query(gsmap.schema.Query, graphene.ObjectType):
    config = graphene.Field(SiteConfigurationNode, language=graphene.String())

    def resolve_config(self, info, language=None):
        config = SiteConfiguration.objects.first()
        config.language = language
        return config


class Mutation(gsmap.schema.Mutation, graphene.ObjectType):
    pass

# pylint: disable=invalid-name
schema = graphene.Schema(query=Query, mutation=Mutation)
