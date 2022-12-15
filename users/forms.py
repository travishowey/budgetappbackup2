from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'form-control bg-success',
        #     }),
        # }


class PaydayForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['payday']
