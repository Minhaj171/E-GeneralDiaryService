from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Show_officer_Dash, name='Show_officer_Dash'),
    path('ShowCrimes/', views.ShowCrimes, name='ShowCrimes'),
    path('Show_ver_requests/', views.Show_ver_requests, name='Show_ver_requests'),
    path('police_reg', views.police_reg, name="police_reg"),
    path('showwlog', views.showwlog, name="showwlog")
]