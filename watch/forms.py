
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Alert,Business


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class AlertForm(forms.ModelForm):
    class Meta:
        model=Alert
        exclude=['post_on','user']


class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['']