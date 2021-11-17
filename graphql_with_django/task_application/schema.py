import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

import tasks.schema
import users.schema

class JWTMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    token_verify = graphql_jwt.Verify.Field()
    token_refresh = graphql_jwt.Refresh.Field()

class Query(
    tasks.schema.Query,
    users.schema.Query, 
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(
    tasks.schema.Mutation,
    users.schema.Mutation,
    JWTMutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)