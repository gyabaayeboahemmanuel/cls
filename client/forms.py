from .models import *
from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("FirstName","LastName", "MiddleName", "PhoneNumber","email", "dateofbirth","GhanaCard", "profile_picture")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields["FirstName" ].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["LastName" ].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["MiddleName"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["email"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["PhoneNumber"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["profile_picture"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["dateofbirth"].widget.attrs.update({'class' :('input--style-4 js-datepicker '),})
        self.fields["GhanaCard"].widget.attrs.update({'class' :('input--style-4'),})
    widgets = {
      'dateofbirth': DateTimeInput(attrs={'type': 'datetime-local'}),
        }