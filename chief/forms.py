from .models import *
from django.forms import ModelForm
class ChiefForm(ModelForm):
    class Meta:
        model = CareTakerChief
        fields = ("StoolName","FullName", "PhoneNumber", "Address")

    def __init__(self, *args, **kwargs):
        super(ChiefForm, self).__init__(*args, **kwargs)
        self.fields["StoolName"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["FullName"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["PhoneNumber"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["Address"].widget.attrs.update({'class' :('input--style-4'),})
