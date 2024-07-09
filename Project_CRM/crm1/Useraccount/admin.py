from django.contrib import admin
from .models import User
# Register your models here.
from django.contrib import admin

#
@admin.register(User)
class CustomUseradmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    search_fields = ['email']