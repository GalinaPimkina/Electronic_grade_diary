from django.contrib import admin
from .models import Teacher, Subject, Group, Student, Grade


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'start_work_date']
    list_display_links = ['name']
    ordering = ['name', 'subject', 'start_work_date']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']
    list_display_links = ['subject']
    ordering = ['subject']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_number', 'group_teacher']
    list_display_links = ['group_number']
    ordering = ['group_number']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'start_study_date']
    list_display_links = ['name']
    ordering = ['name', 'group', 'start_study_date']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade']
    list_display_links = ['grade']
    ordering = ['grade']