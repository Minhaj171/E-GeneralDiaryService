from django.db import models

# Create your models here.
class PoliceVerification(models.Model):
    Verification_id = models.AutoField(primary_key=True)
    Tourist_name = models.CharField(max_length=55,null=False,blank=False)
    Tourist_countrey = models.CharField(max_length=55,null=False,blank=False)
    Tourist_duration = models.CharField(max_length=55)
    Passport_id = models.CharField(max_length=55,null=False,blank=False)

