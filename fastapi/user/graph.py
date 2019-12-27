import graphene
from graphene_pydantic import PydanticObjectType
from user import schemas


class User(PydanticObjectType):
    class Meta:
        model = schemas.User
        only_fields = ('email', 'fullname')
        # exclude_fields = ("id', )
