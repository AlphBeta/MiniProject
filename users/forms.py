from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from .models import Profile,MedInfo

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class DateWidget(forms.DateInput):
    input_type='date'

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        widgets={
            'date_of_birth':DateWidget(),
        }
        model=Profile
        fields=['name','image','blood_group','phone_no','emergency_contact','date_of_birth','donate']

class MedicalInfoForm(forms.ModelForm):

    class Meta:
        model=MedInfo
        fields=['height','weight',]