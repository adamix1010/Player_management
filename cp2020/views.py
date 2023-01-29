from django.shortcuts import render,  reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from .forms import BasicCharacterInfoForm, BasicCharacterStatsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CharacterDetail


class CharacterBasicCreateView(LoginRequiredMixin, CreateView):
    template_name = "CharacterBasic_Create.html"
    form_class = BasicCharacterInfoForm

    def get_success_url(self):
        return reverse("landing-page")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CharacterBasicCreateView, self).form_valid(form)


class BasicCharacterStatsView(LoginRequiredMixin, UpdateView):
    template_name = "CharacterBasicStats_Update.html"
    queryset = CharacterDetail.objects.all()
    form_class = BasicCharacterStatsForm


    def get_success_url(self):
        return reverse("landing-page")
