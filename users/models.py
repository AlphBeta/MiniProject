from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime,date


# Create your models here.
class Profile(models.Model):
    user=OneToOneField(User,on_delete='CASCADE')
    name=models.CharField(max_length=20,default='User')
    image=ImageField(default='default.jpg',upload_to='profile_pics')
    BLOODGROUP_CHOICES=(
        ('AB+','AB+'),('AB-','AB-'),
        ('A+','A+'),('A-','A-'),
        ('B+','B+'),('B-','B-'),
        ('O+','O+'),('O-','O-'),
    )
    
    blood_group=models.CharField(max_length=15,default=None,null=True,choices=BLOODGROUP_CHOICES)
    phone_no=PhoneNumberField(blank=True,max_length=15)
    emergency_contact=PhoneNumberField(blank=True,max_length=15)
    date_of_birth=models.DateField(max_length=8,default=date.today)
    donate=models.BooleanField('Willing to donate?',default=False)
    def calculate_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height> 300:
            outputsize = (300,300)
            img.thumbnail(outputsize)
            img.save(self.image.path)

class MedInfo(models.Model):
    user=OneToOneField(User,on_delete=CASCADE)
    height=models.DecimalField('Height(in cm)',max_digits=5,decimal_places=2,null=True)
    weight=models.DecimalField('Weight(in kg)',max_digits=5,decimal_places=2,null=True)
    #donate=models.BooleanField('Willing to donate?',default=False)

    def __str__(self):
        return self.user.username 