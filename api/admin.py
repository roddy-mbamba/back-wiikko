from django.contrib import admin
from django.contrib.auth.models import Group, User
from  api.models import Message
# Register your models here.
admin.register(Message)
admin.register(User)