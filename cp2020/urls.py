from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import CharacterBasicCreateView, BasicCharacterStatsView
app_name = "CP2020"
urlpatterns = [
    path('create/', CharacterBasicCreateView.as_view(), name="CharBase-Create"),
    path('<int:pk>/basic_stats/', BasicCharacterStatsView.as_view(), name="BaseStats"),
]