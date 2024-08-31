from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    
    phone_number = models.CharField(max_length=10, unique=True,blank=True, null=True)
    # otp = models.CharField(max_length=6, blank=True, null=True)
    # otp_created_at = models.DateTimeField(blank=True, null=True)
    # otp = models.CharField(max_length=6)


    # def generate_otp(self):
    #     self.otp_code = ''.join(random.choices(string.digits, k=6))
    #     self.save()

    # def is_valid(self):
    #     # Add logic for OTP validity duration, e.g., 5 minutes
    #     return not self.is_used and self.created_at + timedelta(minutes=5) > timezone.now()