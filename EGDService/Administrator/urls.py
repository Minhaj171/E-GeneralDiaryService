from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminHome, name='adminHome'),
    path('showComplain/', views.showComplain, name='showComplain'),
    path('ShowVerification/', views.ShowVerification, name='ShowVerification'),
    path('sendComplain/<str:id>', views.sendComplain, name="sendComplain")
]