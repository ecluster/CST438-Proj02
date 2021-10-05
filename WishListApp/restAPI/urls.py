from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('login/', views.login, name = 'login'),
]