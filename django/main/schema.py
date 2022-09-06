import graphene
import gsmap.schema
from django.contrib.gis.db.models import Q
from bs4 import BeautifulSoup
from django_filters import FilterSet, OrderingFilter
from django.conf import settings
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from main.models import ContentSection, SiteConfiguration
import graphene_django_optimizer as gql_optimizer
from main.settings import Q_LANGUAGE

class ContentSectionFilter(FilterSet):
    class Meta:
        model = ContentSection
        fields = ['id', 'is_hero']
    
    order_by = OrderingFilter(
        fields=(
            ('id', 'is_hero')
        )
    )

class ContentSectionNode(DjangoObjectType):
    class Meta:
        model = ContentSection
        fields = [ 'id', 'content', 'is_hero', 'image' ]
        interfaces = [graphene.relay.Node]

    content = graphene.String(
        language_code=graphene.Argument(Q_LANGUAGE, default_value=Q_LANGUAGE[settings.PARLER_DEFAULT_LANGUAGE_CODE]),
    )
    image = graphene.String(
        language_code=graphene.Argument(Q_LANGUAGE, default_value=Q_LANGUAGE[settings.PARLER_DEFAULT_LANGUAGE_CODE]),
    )

    def resolve_content(self, info, language_code=None):
        lang = Q_LANGUAGE.get(language_code).name
        return self.safe_translation_getter("content", language_code=lang)
    
    def resolve_image(self, info, language_code=None):
        lang = Q_LANGUAGE.get(language_code).name
        return self.safe_translation_getter("image", language_code=lang)

class SiteConfigurationNode(gql_optimizer.OptimizedDjangoObjectType):
    class Meta:
        model = SiteConfiguration
        fields = [
            'id', 'search_enabled', 'example_gallery_enabled',
            'homepage_snippet',
        ]
    
    content_sections = DjangoFilterConnectionField(ContentSectionNode, filterset_class=ContentSectionFilter)

    def resolve_homepage_snippet(self, info):
        language = self.language
        soup = BeautifulSoup(self.homepage_snippet, features='html.parser')
        if language:
            found = soup.find(lang=language)
            if found:
                return found
        return soup.div
    
    def resolve_content_sections(self, info, **kwargs):
        return gql_optimizer.query(ContentSectionFilter(kwargs).qs.filter(Q(siteConfiguration_id=self.id)), info)

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
