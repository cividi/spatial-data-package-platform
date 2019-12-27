import graphene
from user.graph import User


class Query(graphene.ObjectType):
    User = graphene.List(User)

    def resolve_user(self, info):
        return get_user()

class Mutation(graphene.ObjectType):
    User = graphene.List(User)

    # def resolve_user(self, info):
    #     return get_user()


schema = graphene.Schema(query=Query)  # mutation=
