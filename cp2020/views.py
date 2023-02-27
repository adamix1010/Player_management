from django.shortcuts import render,  reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from .forms import BasicCharacterInfoForm, BasicCharacterStatsForm, CharacterSkillForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CharacterDetail


class CharacterBasicCreateView(LoginRequiredMixin, CreateView):
    template_name = "CharacterBasic_Create.html"
    form_class = BasicCharacterInfoForm

    def get_success_url(self):
        return reverse("cp2020:BaseStats",kwargs={'pk' : self.object.pk})

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
        return reverse("cp2020:Skills",kwargs={'pk' : self.object.pk})

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.MA_Run = instance.stat_MA * 3
        instance.MA_Leap = instance.MA_Run/3
        instance.MA_Lift = instance.stat_BODY * 10
        instance.EMP_Humanity = instance.stat_EMP * 10
        instance.BODY_Save_Nr = instance.stat_BODY
        instance.save()
        return super(BasicCharacterStatsView, self).form_valid(form)


class CharacterSkillsView(LoginRequiredMixin, UpdateView):
    template_name = "CharacterSkills.html"
    queryset = CharacterDetail.objects.all()
    form_class = CharacterSkillForm


    def get_success_url(self):
        return reverse("landing-page")
