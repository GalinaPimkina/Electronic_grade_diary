from django.db import models


class Teacher(models.Model):
    '''учителя'''

    name = models.CharField(max_length=100, verbose_name='ФИО преподавателя')
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='teacher')
    start_work_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата трудоустройства')

    def __str__(self):
        return f"{self.name}, предмет - {self.subject}"


class Subject(models.Model):
    '''предметы'''

    subject = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.subject


class Group(models.Model):
    '''классы'''

    group_number = models.CharField(max_length=10, verbose_name='Номер группы')
    group_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Классный руководитель', related_name='group')

    def __str__(self):
        return self.group_number


class Student(models.Model):
    '''учащиеся'''

    name = models.CharField(max_length=100, verbose_name='ФИО учащегося')
    age = models.IntegerField(default=0, verbose_name='Возраст учащегося')
    start_study_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, verbose_name='Класс', related_name='student')

    def __str__(self):
        return f"{self.name}, класс - {self.group}"


class Grade(models.Model):
    '''оценки'''

    grade = models.IntegerField(default=1, verbose_name='Оценка')

    def __str__(self):
        return self.grade