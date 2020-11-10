import graphene
import gsmap.schema


class Query(gsmap.schema.Query, graphene.ObjectType):
    pass

class Mutation(gsmap.schema.Mutation, graphene.ObjectType):
    pass

# pylint: disable=invalid-name
schema = graphene.Schema(query=Query, mutation=Mutation)
