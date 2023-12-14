# forms.py
from django import forms
from .models import Message
#from .models import Client


'''class ClientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Set password input as a password field

    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'country', 'password']
'''

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
