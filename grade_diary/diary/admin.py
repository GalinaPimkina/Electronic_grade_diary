from django.contrib import admin

from .forms import UserCreationForm
from .models import Subject, StudyGroup, User


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']
    list_display_links = ['subject']
    ordering = ['subject']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'teacher']
    list_display_links = ['name']
    ordering = ['name', 'subject']
    form = UserCreationForm


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['number']
    list_display_links = ['number']
    ordering = ['number']