from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import User

from main.models import Resume


@admin.register(Resume)
class ResumeAdminView(admin.ModelAdmin):
    list_display = ['user', 'user_id', 'title']