import graphene
from graphene_pydantic import PydanticObjectType
from user import schemas


class User(PydanticObjectType):
    class Meta:
        model = schemas.User
        only_fields = ('id', 'email', 'full_name')
        # exclude_fields = ("id', )
