from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Show_officer_Dash, name='Show_officer_Dash'),
    path('ShowCrimes/', views.ShowCrimes, name='ShowCrimes'),
    path('Show_ver_requests/', views.Show_ver_requests, name='Show_ver_requests'),
]