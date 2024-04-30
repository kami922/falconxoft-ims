from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput

from core.models import Equipment,Reservation

#adminApp form

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["password1","password2","username","email"]   

    
class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ('assigned_to',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpu'].required = False
        self.fields['gpu'].required = False
        # Optional: Set placeholder text for clarity
        self.fields['cpu'].widget.attrs['placeholder'] = 'Enter CPU details (Optional)'
        self.fields['gpu'].widget.attrs['placeholder'] = 'Enter GPU details (Optional)'
