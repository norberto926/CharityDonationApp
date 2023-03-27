from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm, SelectMultiple, Select, TextInput, DateInput, TimeInput, CheckboxSelectMultiple, \
    RadioSelect, NumberInput, Textarea

from donation.models import User, Donation, Category, Institution
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserModel
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Imię'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}), label='')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label='')


class DonationForm(forms.ModelForm):

    quantity = forms.IntegerField(label='', widget=TextInput(attrs={'name': 'bags', 'type': 'number'}))
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label="",
                                                widget=CheckboxSelectMultiple(attrs={'name': 'categories'}))
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(), label="",
                                         widget=RadioSelect(attrs={'name': 'organization'}))
    address = forms.CharField(max_length=255, label="", widget=TextInput(attrs={'name': 'address'}))
    phone_number = PhoneNumberField(max_length=64, label="", widget=PhoneNumberInternationalFallbackWidget(attrs={'name': 'phone '}))
    city = forms.CharField(max_length=64, label="", widget=TextInput(attrs={'name': 'city'}))
    zip_code = forms.CharField(max_length=64, label="", widget=TextInput(attrs={'name': 'postcode'}))
    pick_up_date = forms.DateField(label="", widget=DateInput(attrs={'name': 'data', 'type': 'date'}))
    pick_up_time = forms.TimeField(label="", widget=TimeInput(attrs={'name': 'time', 'type': 'time'}))
    pick_up_comment = forms.CharField(max_length=255, label="", widget=Textarea(attrs={'name': 'more_info', 'rows': '5'}))

    class Meta:
        model = Donation
        fields = ['quantity', 'categories', 'institution', 'address', 'phone_number', 'city',
                  'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment']



