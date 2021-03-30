from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Imageloader

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1','password2']
class Imageform(forms.ModelForm):
    class Meta:
        model = Imageloader
        fields = '__all__'
        labels = {'photo':''}