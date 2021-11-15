import graphene
from graphene_django import DjangoObjectType
from .models import User

class RegisterType(graphene.ObjectType):
    message = graphene.String()
    id = graphene.Int()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'is_active',
        )