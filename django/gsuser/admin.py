from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from graphene import relay

admin.site.register(User, UserAdmin)
