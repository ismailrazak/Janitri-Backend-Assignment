from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="patient_profile")
    medical_record = models.TextField()



class HeartData(models.Model):
    # heart_rate in bpm
    heart_rate = models.IntegerField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile,on_delete=models.CASCADE,related_name="heart_data")

