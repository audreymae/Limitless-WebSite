from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True)  # Height in meters
    weight = models.FloatField(null=True, blank=True)  # Weight in kilograms
    fitness_goal = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
