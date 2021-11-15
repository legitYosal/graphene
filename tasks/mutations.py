import graphene
from .types import TaskType
from .models import Task

class TaskArgumants:
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    user = graphene.Int()
    status = graphene.String()
    due_date = graphene.DateTime()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()


class CreateTask(graphene.Mutation):
    class Arguments(TaskArgumants):
        pass

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = Task.objects.create(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            user_id=kwargs.get('user'),
            # status=kwargs.get('status'),
            due_date=kwargs.get('due_date'),
        )
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    class Arguments(TaskArgumants):
        pass

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = Task.objects.get(id=kwargs.get('id'))
        task.title = kwargs.get('title', task.title)
        task.description = kwargs.get('description', task.description)
        # task.user = kwargs.get('user')
        task.status = kwargs.get('status', task.status)
        task.due_date = kwargs.get('due_date', task.due_date)
        task.save()
        return UpdateTask(task=task)

class DeleteTask(graphene.Mutation):
    class Arguments(TaskArgumants):
        pass

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = Task.objects.get(id=kwargs.get('id'))
        task.delete()
        return None