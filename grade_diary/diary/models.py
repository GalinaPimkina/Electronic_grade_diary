from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    '''предметы'''

    subject = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.subject


class Teacher(User):
    '''учителя'''

    name = models.CharField(max_length=100, verbose_name='ФИО преподавателя')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name='Преподаватель', related_name='teacher')

    def __str__(self):
        return self.name


class Student(User):
    '''учащиеся'''

    name = models.CharField(max_length=100, verbose_name='ФИО учащегося')
    born_date = models.DateTimeField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name


class Grade(models.Model):
    '''оценки'''

    grade = models.IntegerField(default=1, verbose_name='Оценка')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='grade')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name='Оценки', related_name='grade')


class StudyGroup(models.Model):
    '''учебная группа (класс)'''

    number = models.CharField(max_length=10, verbose_name='Номер учебной группы')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name='Учащийся', related_name='study_group')
    group_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='Классный руководитель', related_name='study_group')
