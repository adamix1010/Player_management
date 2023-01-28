from django import forms
from .models import CharacterDetail
from django.contrib.auth.forms import UserCreationForm, UsernameField


class BasicCharacterInfoForm(forms.ModelForm):
    class Meta:
        model = CharacterDetail
        fields = (
            'name',
            'role',
            'picture',
        )
