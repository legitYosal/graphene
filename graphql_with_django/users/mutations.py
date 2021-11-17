import graphene
from .types import UserType
from .models import User


class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.create(
            email=kwargs.get('email'),
            password=kwargs.get('password'),
            is_active=False,
        )
        return RegisterUser(user=user)

class ActivateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id'))
        user.is_active = True
        user.save()
        return ActivateUser(user=user)