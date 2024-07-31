from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_permissions = models.ManyToManyField('auth.Permission',
                                              related_name='%(class)s_user_permissions',
                                              blank=True,
                                              help_text='Specific permissions for this user.',
                                              verbose_name='user permissions',
                                              )


