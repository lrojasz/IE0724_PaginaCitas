"""
gymnasium URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

# Incluir patrones y los urls del scheduler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduler.urls')),
]
