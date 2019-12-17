from django.urls import path, include
from .import views

urlpatterns = [
    path('user_dashboard/', views.userPage, name="userPage"),
    path('userComplain', views.userComplain, name="userComplain"),
    path('user_verr', views.user_verr, name="user_verr")

]