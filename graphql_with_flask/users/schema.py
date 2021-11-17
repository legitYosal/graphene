import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from config import User, db

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User


class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User(
            email=kwargs.get('email'),
            password=kwargs.get('password'),
            active=False,
        )
        db.session.add(user)
        db.session.commit()
        return RegisterUser(user=user)

class ActivateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.query.get(kwargs.get('id'))
        user.active = True
        db.session.commit()
        return ActivateUser(user=user)

class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    activate_user = ActivateUser.Field()

class Query(graphene.ObjectType):
    user = graphene.Field(UserType)
    def resolve_user(self, info, **kwargs):
        """This is actually the get profile"""
        # user = info.context.user
        user = User.query.get(1)
        return user