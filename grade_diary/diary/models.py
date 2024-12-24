from django.db import models
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):
    '''предметы'''

    subject = models.CharField(max_length=100, null=True, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('subject', )

    def __str__(self):
        return self.subject


class User(AbstractUser):

    name = models.CharField(max_length=100, verbose_name='ФИО')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Предмет', related_name='teacher')
    born_date = models.DateField(null=True, verbose_name='Дата рождения')
    teacher = models.BooleanField(default=False, verbose_name='Преподаватель')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('name', )

    def __str__(self):
        return self.name


class GradeTable(models.Model):
    '''оценки'''

    grade = models.IntegerField(default=1, verbose_name='Оценка')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='grade')
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Оценки', related_name='grade')

    class Meta:
        verbose_name = 'Журнал оценок'
        verbose_name_plural = 'Журнал оценок'
        ordering = ('subject', )


class StudyGroup(models.Model):
    '''учебная группа (класс)'''

    number = models.CharField(max_length=10, verbose_name='Номер учебной группы')
    students = models.ManyToManyField(User, verbose_name='Учащийся')

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ('number', )

    def __str__(self):
        return f"класс - {self.number}"
