import graphene
from graphql_jwt.decorators import login_required
from .models import Task
from .types import TaskType
from . import mutations

class Mutation(graphene.ObjectType):
    create_task = mutations.CreateTask.Field()
    update_task = mutations.UpdateTask.Field()
    delete_task = mutations.DeleteTask.Field()

class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    @login_required
    def resolve_tasks(root, info, **kwargs):
        return Task.objects.filter(
            user=info.context.user
        )