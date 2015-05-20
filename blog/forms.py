from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
__author__ = 'clay'


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    #then we need to point it to what model we want to pull it from (we are grabbing the defaults and adding email)
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']