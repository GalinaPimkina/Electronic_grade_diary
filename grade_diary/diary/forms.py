from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from diary.models import StudyGroup
from diary.utils import create_password


class UserRegisterForm(forms.ModelForm):
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    # password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username',  'email', 'name', 'teacher',
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

    def clean_password(self):
        '''метод переопределен, чтобы система автоматически генерировала пароль при создании нового пользователя '''

        return create_password()

    def save(self, commit=True):
        '''метод переопределен, чтобы при создании нового юзера/редактировании старого, генерировался и сохранялся новый пароль'''
        user = super().save(commit=False)
        user.set_password(self.clean_password())

        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user


class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ['number', 'students']
