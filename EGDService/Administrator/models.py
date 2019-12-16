from django.db import models

# Create your models here.
class adminn(models.Model):
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=10, blank=False)

class policeComplain(models.Model):
    Complain_type = models.CharField(max_length=55)
    Complainant_name = models.CharField(max_length=55)
    Mobile_Number = models.CharField(max_length=55)
    National_id = models.CharField(max_length=55)
    District = models.CharField(max_length=55)
    Thana = models.CharField(max_length=55)
    Address = models.CharField(max_length=55)
    Complain_description = models.CharField(max_length=55)
    Email = models.EmailField(max_length=50, blank=False, unique=True)
