from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='teacher')

    def __str__(self):
        return f"{self.surname} {self.name}, предмет - {self.subject}"


class Subject(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Предмет')
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, verbose_name='Ученик', related_name='subject')
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, verbose_name='Оценка', related_name='grade')

    def __str__(self):
        return self.subject


class Group(models.Model):
    group_number = models.CharField(max_length=10, verbose_name='Номер группы')
    group_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Классный руководитель', related_name='group')

    def __str__(self):
        return self.group_number


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст учащегося')
    start_study_date = models.IntegerField(default=0, verbose_name='Дата начала обучения')
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, verbose_name='Класс', related_name='student')

    def __str__(self):
        return f"{self.surname} {self.name}, класс {self.group}"


class Grade(models.Model):
    mark = models.IntegerField(default=1, verbose_name='Оценка')

    def __str__(self):
        return self.mark
