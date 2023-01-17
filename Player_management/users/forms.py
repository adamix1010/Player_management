from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}
