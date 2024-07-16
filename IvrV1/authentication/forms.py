# authentication/forms.py

from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dob', 'doa', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AuthenticateForm(forms.Form):
    id = forms.IntegerField(label='ID')
    dob = forms.DateField(label='Date of Birth')
    doa = forms.DateField(label='Date of Arrival')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
