from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from diary.models import StudyGroup


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'name', 'teacher',
                  'subject', 'born_date', 'is_staff', 'user_permissions', 'groups', 'is_active', 'date_joined']
        labels = {
            'username': 'Логин',
            'email': 'E-mail',
            'name': 'ФИО',
            'teacher': 'Статус - преподаватель',
            'subject': 'Предмет',
            'born_date': 'Дата рождения',
            'is_staff': 'Статус - персонал',
            'is_active': 'Статус - Активный пользователь',
            'date_joined': 'Дата регистрации',
            'user_permissions': 'Права пользователя',
            'groups': 'Группа пользователей'
        }


class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ['number', 'students']
