from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="patient_profile")
    medical_record = models.TextField()

    def __str__(self):
        return f"{self.user.username}_patient_profile"

class HeartData(models.Model):
    # heart_rate in bpm
    heart_rate = models.IntegerField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile,on_delete=models.CASCADE,related_name="heart_data")

    def __str__(self):
        return f"{self.heart_rate}_{self.timestamp}"
