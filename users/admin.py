from django.contrib import admin
from .models import Profile,MedInfo,Doctor

# Register your models here.
admin.site.register(Profile)
admin.site.register(MedInfo)
admin.site.register(Doctor)
