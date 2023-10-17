from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpform(UserCreationForm):
    username = forms.CharField(label="Логин",
                               help_text= '')
    password1 = forms.CharField(label= 'Пароль',
                                help_text= '', widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    password2 = forms.CharField(label='Подтверждение',
                                help_text= '', widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))

    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'placeholder':'qwe@mail.ru'}))
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(label='Фамилия', max_length=20, required=False)