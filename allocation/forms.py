from .models import *
from django.forms import ModelForm

class AllocationForm(ModelForm):
    class Meta:
        model = Allocation 
        # fields= ()
        fields = ("receiptno", "land", "CareTakerChief", "client")
