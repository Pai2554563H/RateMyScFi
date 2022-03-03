from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        db_table = 'a_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name
