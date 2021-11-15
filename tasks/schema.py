import graphene
from .models import Task
from .types import TaskType
from . import mutations

class Mutation(graphene.ObjectType):
    create_task = mutations.CreateTask.Field()
    update_task = mutations.UpdateTask.Field()
    delete_task = mutations.DeleteTask.Field()

class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(root, info, **kwargs):
        return Task.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)