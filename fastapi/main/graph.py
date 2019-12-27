import graphene
from user.graph import User
from user.models import UserModel
from typing import Optional

from sqlalchemy.orm import Session
from main.database import db_session


def get_user(db: Session = db_session, *, id: int):
    users = db.query(UserModel).filter(UserModel.id == id).first()
    return user


def get_users(db: Session=db_session):
    users = db.query(UserModel).all()
    return users


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return get_users()


schema = graphene.Schema(query=Query)
