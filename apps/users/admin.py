from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    #fields = ('username', 'email', 'password')
    list_display = ('username', 'email', 'last_login')


admin.site.register(User, UserAdmin)