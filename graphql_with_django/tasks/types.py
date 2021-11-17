from graphene_django import DjangoObjectType
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'user',
            'status',
            'due_date',
            'created_at',
            'updated_at',
        )