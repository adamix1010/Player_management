from django.shortcuts import render,  reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


def landing_page(request):

    return render(request, "landing.html")

