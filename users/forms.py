from django.contrib.auth.forms import UserCreationForm, UsernameField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit',
                            css_class='text-white bg-green-500 border-0 py-2 px-8 focus:outline-none hover:bg-green-600 rounded text-lg'))
    helper.form_method = 'POST'