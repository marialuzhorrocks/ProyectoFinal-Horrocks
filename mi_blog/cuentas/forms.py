from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
