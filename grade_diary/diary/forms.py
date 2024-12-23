from django.forms import ModelForm

from diary.models import User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'teacher',
                  'subject', 'born_date', 'is_staff', 'is_active', 'date_joined']