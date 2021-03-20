from typing import Tuple
from users.models import MedInfo, Profile
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,MedicalInfoForm
from .models import MedInfo

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':    
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request,f'Profile Updated {username}')
            return redirect('medicalinfo')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'profile.html',context)

@login_required
def medinfo(request):
    if request.method=='POST':    
        u_form=UserUpdateForm(request.POST,instance=request.user)
        m_form=MedicalInfoForm(request.POST,instance=request.user.medinfo)
        if m_form.is_valid():
            m_form.save()
            messages.success(request,f'Medical Data Updated Successfully')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        m_form=MedicalInfoForm(instance=request.user.medinfo)
    
    context={
        'u_form':u_form,
        'm_form':m_form,
    }
    return render(request,'medinfo.html',context)

@login_required
def blood_donation(request):
    donors=User.objects.filter(profile__donate=True).all
    
    context={
        'donors_list':donors,
        'count':1,
   }
    return render(request,'blood_donation.html',context)

@login_required
def profile_info(request):
    users=User.objects.all().order_by('-medinfo__score')
    context={
        'users':users
    }
    return render(request,'profile_info.html',context)