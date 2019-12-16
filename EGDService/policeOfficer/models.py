from django.db import models

# Create your models here.
class police(models.Model):
    thana = models.CharField(max_length=100, blank=False, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=11, blank=False)