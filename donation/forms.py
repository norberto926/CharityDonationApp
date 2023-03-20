from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Imię'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}), label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'username']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label='')
