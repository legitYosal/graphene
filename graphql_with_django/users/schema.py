import graphene
from graphql_jwt.decorators import login_required
from .models import User
from .types import UserType
from . import mutations

class Mutation(graphene.ObjectType):
    register_user = mutations.RegisterUser.Field()
    activate_user = mutations.ActivateUser.Field()

class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    @login_required
    def resolve_user(self, info, **kwargs):
        """This is actually the get profile"""
        user = info.context.user
        return user