from django.urls import path, include
from .import views

urlpatterns = [
    # path('', views.show_index, name='show_index'),
    path('', views.show_log, name='show_log'),
    path('userlogin', views.userlogin, name="userlogin"),
    path('User_registration', views.User_registration, name="User_registration")
]