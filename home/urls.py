from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('tips/', views.tips_page, name='tips'),
    path('support/', views.support_page, name='support'),
]