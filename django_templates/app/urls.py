from django.contrib import admin
from django.urls import path, include
from .views import *
import django_adminlte

urlpatterns = [
    path('home', index, name='home'),
    path('contact/<id>', contact, name='contact'),
    path('about', about, name='about'),
]
