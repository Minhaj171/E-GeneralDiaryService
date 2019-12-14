from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.show_index, name='touristlist'),
    path('P_Verification/', views.user_ver, name='police_verification'),


]