from django import forms
from .models import Drug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'quantity', 'status', 'remain']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
