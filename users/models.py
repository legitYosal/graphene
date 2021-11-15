from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    USERNAME_FIELD = 'email'
