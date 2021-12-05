from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from pet_project.security.models import AbstractBaseModel

username_validator = UnicodeUsernameValidator()


class User(PermissionsMixin, AbstractBaseUser, AbstractBaseModel):
    username = models.CharField('Username', max_length=255, unique=True, validators=[username_validator])
    email = models.EmailField('Email address', blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    password = None
    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [EMAIL_FIELD]

    @property
    def is_django_user(self):
        return self.has_usable_password()
