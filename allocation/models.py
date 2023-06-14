from django.db import models
from chief.models import *
from lands.models import Land
from client.models import *
# Create your models here.

class Allocation(models.Model):
    receiptno = models.CharField(max_length=255)
    dateofallocation = models.DateField(auto_now=True)
    land = models.OneToOneField(Land, on_delete=models.CASCADE, related_name='allocated')
    CareTakerChief = models.OneToOneField(CareTakerChief, on_delete=models.CASCADE, related_name='chief')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
