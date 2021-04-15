from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from .models import Profile,MedInfo,Doctor

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
            'sex':widgets.RadioSelect()
        }
        model=Profile
        fields=['name','image','blood_group','phone_no','emergency_contact','date_of_birth','donate']

class MedicalInfoForm(forms.ModelForm):

    class Meta:
        widgets={
            'fever_cycle':widgets.RadioSelect(),
            'fever':widgets.RadioSelect(),
            'eye_sight':widgets.RadioSelect(),
            'sex': widgets.RadioSelect(),
            'diabetes':widgets.RadioSelect()
        }
        model=MedInfo
        fields=['height','weight','sex','waist','hip','diabetes','is_athlete','pulse','fever','fever_cycle','eye_sight']

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['doctor_name', 'qualification', 'specialization','phone_no','image','email','document','postal_code']