from django.db import models


# Create your models here.
class user_reg(models.Model):
    user_email = models.EmailField(max_length=100, blank=False, unique=True, primary_key=True)
    user_password = models.CharField(max_length=55)
    user_name = models.CharField(max_length=55)
    user_phone = models.CharField(max_length=55)
