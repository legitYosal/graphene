import graphene

import tasks.schema
import users.schema

class Query(
    tasks.schema.Query,
    users.schema.Query,
    graphene.ObjectType
): 
    pass

class Mutation(
    tasks.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
