from django.db import models


class Subject(models.Model):
    '''предметы'''

    subject = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.subject


class Student(models.Model):
    '''учащиеся'''

    name = models.CharField(max_length=100, verbose_name='ФИО учащегося')

    def __str__(self):
        return self.name


class Grade(models.Model):
    '''оценки'''

    grade = models.IntegerField(default=1, verbose_name='Оценка')
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='grade')
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, verbose_name='Оценки', related_name='grade')


