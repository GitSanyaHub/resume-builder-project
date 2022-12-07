from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя-----', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email----', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пороль-', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Пороль-', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин----', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пороль--', widget=forms.PasswordInput(attrs={'class': 'form-input'}))




