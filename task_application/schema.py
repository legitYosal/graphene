import tasks.schema
import graphene
from graphene_django.debug import DjangoDebug

class Query(
    tasks.schema.Query, 
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(
    tasks.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)