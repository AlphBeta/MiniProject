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
    age=models.IntegerField(default=None)
    def calculate_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.age=self.calculate_age()
        if self.age<18:
            self.donate=False
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height> 300:
            outputsize = (300,300)
            img.thumbnail(outputsize)
            img.save(self.image.path)

class MedInfo(models.Model):
    Bmi_grade={
        'N':'Normal',
        'U':'UnderWeight',
        'O':'OverWeight',
        'OO':'Obese'
    }
    FEVER={
    ('S','Very Often'),
    ('N','Once in a while'),
    ('NN',"Don't remember the last time I got")
    }
    score=models.IntegerField(default=50,blank=True)
    user=OneToOneField(User,on_delete=CASCADE)
    height=models.DecimalField('Height(in cm)',max_digits=5,decimal_places=2,null=True)
    weight=models.DecimalField('Weight(in kg)',max_digits=5,decimal_places=2,null=True)
    is_athlete=models.BooleanField("Are you an Athlete:",default=False)
    bmi_grade=models.CharField(max_length=20,null=True,default=None)
    pulse=models.IntegerField('Pulse rate',blank=True,default=50,null=True)
    bmi=models.DecimalField(max_digits=5,decimal_places=2,default=None)
    fever=models.BooleanField('Are you ill/Having Cold?',default=False,choices=((True,'Yes'),(False,'No')))
    fever_cycle=models.CharField('How often do you get cold or fever?',max_length=3,default=None,null=True,choices=FEVER)


    #donate=models.BooleanField('Willing to donate?',default=False)

    def bmi_analyze(self):
        height=self.height/100
        self.bmi=(self.weight)/(height*height)
        if self.bmi<=18.5:
            self.score-=3
            self.bmi_grade=self.Bmi_grade['U']
        elif self.bmi>=25 and self.bmi<=29.9:
            self.score-=3
            self.bmi_grade=self.Bmi_grade['O']
        elif self.bmi>30:
            self.bmi-=5
            self.bmi_grade=self.Bmi_grade['OO']
        else:
            self.score+=3
            self.bmi_grade=self.Bmi_grade['N']
        
    def pulse_analyze(self):
        self.score=50
        if self.is_athlete:
            if self.pulse>85 or self.pulse<=33:
                self.score=self.score-3
            else:
                self.score=50
        else:
            if self.pulse>85 or self.pulse<55:
                self.score=self.score-3
            else:
                self.score=50

    def fever_calc(self):
        if self.fever:
            self.score-=5
        if(self.fever_cycle=='S'):
            self.score-=3
        elif(self.fever_cycle=='NN'):
            self.score+=3
            
    def __str__(self):
        return self.user.username 
    
    def save(self, *args, **kwargs):
        self.pulse_analyze()
        super().save( *args, **kwargs)
        self.bmi_analyze()            #saving the score
        super().save( *args, **kwargs)
        self.fever_calc()
        super().save( *args, **kwargs)