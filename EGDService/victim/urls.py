from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.showvictim, name='victimlist'),
    path('login', views.loginPage, name='loginPage')

uyktgu
]