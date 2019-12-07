from django.db import models


# Create your models here.
class Complain(models.Model):
    Complain_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    Complain_type = models.CharField(max_length=55)
    Complainant_name = models.CharField(max_length=55)
    Mobile_Number = models.CharField(max_length=55)
    National_id = models.CharField(max_length=55)
    District = models.CharField(max_length=55)
    Thana = models.CharField(max_length=55)
    Address = models.CharField(max_length=55)
    Complain_description = models.CharField(max_length=55)
    Email = models.EmailField(max_length=50, blank=False, unique=True)
