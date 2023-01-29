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


class BasicCharacterStatsForm(forms.ModelForm):
    class Meta:
        model = CharacterDetail
        fields = (
            'stat_INT',
            'stat_REF',
            'stat_TECH',
            'stat_COOL',
            'stat_ATTR',
            'stat_LUCK',
            'stat_MA',
            'stat_BODY',
            'stat_EMP',
        )
