from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class StaffForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2 
    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ('profile_picture',)
    # def clean(self):
    #     cleaned_data = super(Profile, self).clean()
        # self.fields['user'].widget.attrs.update({
        # #             'styles': ('display:none')
        # })
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["password"].widget.attrs.update({'class' :('input--style-4'),})
        self.fields["email"].widget.attrs.update({'class' :('input--style-4'),})

    