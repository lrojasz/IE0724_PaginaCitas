"""
gymnasium URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

# Incluir patrones y los urls del scheduler
urlpatterns = [
    path('',views.home, name='home'),
    path('home/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('schedule/', views.schedule, name="schedule"),
    path('nosotros/', views.about_us, name="about_us"),
    path('gallery/', views.gallery, name="gallery"),
]
