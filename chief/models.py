from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CareTakerChief (models.Model):
    # chiefid = models.CharField(primary_key=True,auto_created=True, editable=False, max_length=10, unique=True)
    ctchief = models.OneToOneField(User, on_delete=models.CASCADE)
    StoolName = models.CharField(max_length=255, verbose_name="Stool Name")
    FullName = models.CharField(max_length=255, verbose_name="full Name")
    PhoneNumber = models.CharField(max_length=255, verbose_name="Phone Number")
    Address = models.CharField(max_length=255, verbose_name="Address")
    
    def __str__(self):
        return self.StoolName
    