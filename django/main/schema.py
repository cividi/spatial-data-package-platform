import graphene
import gsmap.schema


class Query(gsmap.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
