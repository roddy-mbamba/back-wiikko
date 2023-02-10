from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage
from django.core import validators
from django.db.models.fields import CharField, related
from django.db.models.enums import Choices
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.base import Model
from django.core.files import storage
from django.contrib.auth.models import Group, User
from django.contrib.admin import autodiscover
from django.db import models
# Create your models here.


class Message(models.Model):

    msg = models.TextField(null=False,blank=False)
    createAt = models.DateTimeField(auto_now_add=True, null=True)
    updateAt = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(
        User, related_name="message_user", null=False)

    def __str__(self):
        return self.msg

