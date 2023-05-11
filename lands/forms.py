from .models import *
from django.forms import ModelForm
class LandForm(ModelForm):
    class Meta:
        model = Land
        fields = ("plot","block", "sector", "location")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields["plot" ].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["block" ].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["sector"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["location"].widget.attrs.update({'class' :('input--style-4'),})
    def clean(self):
        cleaned_data = super(LandForm, self).clean()