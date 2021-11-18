import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from config import Task, db

class TaskType(SQLAlchemyObjectType):
    class Meta:
        model = Task


class TaskArgumants:
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    # user = graphene.Int()
    status = graphene.Argument(
        graphene.Enum('TaskStatuses', [
            (key.value, Task.TaskStatus(key).value) for key in Task.TaskStatus
        ])
    )
    due_date = graphene.DateTime()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()


class CreateTask(graphene.Mutation):
    class Arguments(TaskArgumants):
        pass

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = Task(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            user=info.context.user,
            due_date=kwargs.get('due_date'),
        )
        db.session.add(task)
        db.session.commit()
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    class Arguments(TaskArgumants):
        pass

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = Task.query.filter_by(
            id=kwargs.get('id'),
            user=info.context.user,
        ).first_or_404()
        task.title = kwargs.get('title', task.title)
        task.description = kwargs.get('description', task.description)
        # task.user = kwargs.get('user')
        task.status = kwargs.get('status', task.status)
        task.due_date = kwargs.get('due_date', task.due_date)
        db.session.commit()
        return UpdateTask(task=task)

class DeleteTask(graphene.Mutation):
    class Arguments(TaskArgumants):
        pass

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = Task.query.filter_by(
            id=kwargs.get('id'),
            user=info.context.user,
        ).first_or_404().delete()
        db.session.commit()
        return None


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)
    def resolve_tasks(root, info, **kwargs):
        return Task.query.filter_by(user=info.context.user)


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()