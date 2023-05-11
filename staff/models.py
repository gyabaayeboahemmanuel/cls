from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile (models.Model):
    user = models.OneToOneField(User,  on_delete= models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to = "profile/", null=True, blank=True)
    dateSignedUp = models.DateTimeField(auto_now_add=True)