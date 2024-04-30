from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput

from .models import Equipment,Reservation

#user Core forms

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
        fields = "__all__"
        # exclude = ("assigned_to",)