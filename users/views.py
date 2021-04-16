import re
from typing import Tuple
from users.models import MedInfo, Profile,Doctor
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,MedicalInfoForm,DoctorProfileForm
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
            return redirect('profile_info')
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
    if request.method=='POST':
        user=request.user
        u=user.profile.postal_code
        blood=request.POST.get('choice',None)
        donors=User.objects.filter(profile__donate=True,profile__blood_group=blood).all().order_by('profile__postal_code'-u)
        context={
            'donors_list':donors,
            'count':1,
        }
        return render(request,'blood_donation.html',context)
    else:
        return render(request,'blood_donation.html')

@login_required
def leaderboard(request):
    users=User.objects.all().order_by('-medinfo__score')[:15]
    context={
        'users':users
    }
    return render(request,'leaderboard.html',context)

@login_required
def profile_info(request):
    user=request.user
    return render(request,'profile_info.html',{'user':user})

def about(request):
    return render(request,'about.html')

def doc_profile(request):
    if request.method=='POST':    
        d_form=DoctorProfileForm(request.POST,request.FILES)
        if d_form.is_valid():
            d_form.save()
            messages.success(request,f'Successfully added Doctor\'s Information')
            return redirect('MedEbook')
    else:
        d_form=DoctorProfileForm()

    context={
        'd_form':d_form,
    }
    return render(request,'doc_profile.html',context)

@login_required
def list_of_doctor(request):
    us=request.user
    u=us.profile.postal_code
    doctors=Doctor.objects.order_by(F('postal_code') - u).all
    context={
        'doctors':doctors,
        'count':1,
    }
    return render(request, 'doc_list.html', context)

@login_required
def suggestion(request):
    user=request.user
    return render(request,'suggestion.html',{'user':user})