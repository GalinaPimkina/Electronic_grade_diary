from django.db import models


class Subject(models.Model):
    '''предметы'''

    subject = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.subject


class Student(models.Model):
    '''учащиеся'''

    name = models.CharField(max_length=100, verbose_name='ФИО учащегося')
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, verbose_name='Оценки', related_name='student')

    def __str__(self):
        return {self.name}


class Grade(models.Model):
    '''оценки'''

    GRADE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    grade = models.IntegerField(choices=GRADE_CHOICES, default=GRADE_CHOICES[0], verbose_name='Оценка')
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='grade')

    def __str__(self):
        return self.grade

