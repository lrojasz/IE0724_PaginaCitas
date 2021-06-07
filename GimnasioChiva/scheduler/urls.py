"""
gymnasium URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

# Incluir patrones y los urls del scheduler
urlpatterns = [
    path('', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
]
