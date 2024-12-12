from django.contrib import admin
from .models import Subject, Student, Grade


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']
    list_display_links = ['subject']
    ordering = ['subject']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    ordering = ['name']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade']
    list_display_links = ['grade']
    ordering = ['grade']