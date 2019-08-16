from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from main import views



urlpatterns = [
    path('', TemplateView.as_view(template_name="main/home.html"), name='home'),
]