import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from config import User, db

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class Mutation(graphene.ObjectType):
    pass