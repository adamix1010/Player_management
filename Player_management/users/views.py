from django.shortcuts import render,  reverse
from django.views.generic import CreateView
from .forms import UserCreationForm


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")
