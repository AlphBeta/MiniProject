#from users.views import profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField
from PIL import Image
from django.http import request
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.decorators import login_required
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
    postal_code=models.IntegerField(default=None,null=True,blank=False)
    donate=models.BooleanField('Willing to donate?',default=False)
    sex = models.CharField(max_length=7,default=None,null=True,choices=(('M','Male'),('F','Female'),('O','Other')))
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
    Whr_grade={
        'L':'LOW',
        'M':'MODERATE',
        'S':'HIGH',
        'N':'NULL'
    }
    FEVER={
    ('S','Very Often'),
    ('N','Once in a while'),
    ('NN',"Don't remember the last time I got")
    }
    SIGHT={
        ('Normal','I can see clearly'),
        ('Glasses','I wear Glasses'),
        ('Myopia','Difficult to see distant objects'),
        ('Hypermetropia','Difficult in reading'),
        ('Presbyopia','Difficulty in both')
    }
    score=models.IntegerField(default=50,blank=True)
    user=OneToOneField(User,on_delete=CASCADE)
    sex = models.CharField(max_length=7,default=None,null=True,choices=(('M','Male'),('F','Female'),('O','Other')))
    height=models.DecimalField('Height(in cm)',max_digits=5,decimal_places=2,null=True)
    weight=models.DecimalField('Weight(in kg)',max_digits=5,decimal_places=2,null=True)
    waist=models.DecimalField('Waist(in cm)',max_digits=5,decimal_places=2,null=True,blank=True)
    hip=models.DecimalField('Hip(in cm)',max_digits=5,decimal_places=2,null=True,blank=True)
    is_athlete=models.BooleanField("Are you an Athlete:",default=False)
    bmi_grade=models.CharField(max_length=20,null=True,default=None)
    whr_grade=models.CharField(max_length=20,null=True,default=None)
    pulse=models.IntegerField('Resting Heart Rate',blank=True,default=None,null=True)
    bmi=models.DecimalField(max_digits=5,decimal_places=2,default=19)
    whr=models.DecimalField(max_digits=5,decimal_places=2,default=None,null=True)
    diabetes=models.BooleanField('Do you have diabetes?',default=False,choices=((True,'Yes'),(False,'No')))
    fever=models.BooleanField('Are you ill/Having Cold?',default=False,choices=((True,'Yes'),(False,'No')))
    fever_cycle=models.CharField('How often do you get cold or fever?',max_length=3,default=None,null=True,choices=FEVER)
    eye_sight=models.CharField("How is your eye sight?",max_length=20,default=False,choices=SIGHT)


    #donate=models.BooleanField('Willing to donate?',default=False)

    def bmi_analyze(self,score):
        self.score=score
        if self.height or self.weight:
            height=self.height/100
            self.bmi=(self.weight)/(height*height)
            if self.bmi<=18.5:
                self.score-=3
                self.bmi_grade=self.Bmi_grade['U']
            elif self.bmi>=25 and self.bmi<=29.9:
                self.score-=3
                self.bmi_grade=self.Bmi_grade['O']
            elif self.bmi>30:
                self.score-=5
                self.bmi_grade=self.Bmi_grade['OO']
            else:
                self.score+=3
                self.bmi_grade=self.Bmi_grade['N']
        return self.score
        
    def whr_analyze(self,score):
        self.score=score
        if self.hip or self.waist:
            self.whr=self.waist/self.hip
            if(self.sex=='F'):
                if self.whr<=0.8:
                    self.score+=5
                    self.whr_grade=self.Whr_grade['L']
                elif self.whr>=0.81 and self.whr <=0.85:
                    self.score+=3
                    self.whr_grade=self.Whr_grade['M']
                elif self.whr>0.85:
                    self.score-=5
                    self.whr_grade=self.Whr_grade['S']
            else:
                if self.whr<=0.95:
                    self.score+=5
                    self.whr_grade=self.Whr_grade['L']
                elif self.whr>=0.96 and self.whr <=1:
                    self.score+=3
                    self.whr_grade=self.Whr_grade['M']
                elif self.whr>1:
                    self.score-=5
                    self.whr_grade=self.Whr_grade['S']
        else:
            self.whr_grade=self.Whr_grade['N']
        return self.score

    def pulse_analyze(self):
        self.score=50
        if self.pulse:
            if self.is_athlete:
                if self.pulse>85 or self.pulse<=33:
                    self.score-=3
                else:
                    self.score=50
            else:
                if self.pulse>85 or self.pulse<55:
                    self.score-=3
                else:
                    self.score=50
        return self.score

    def diab_analyze(self,score):
        self.score=score
        if self.diabetes:
            self.score-=3
        else:
            self.score+=1
        return self.score

    def fever_calc(self,score):
        self.score=score
        if self.fever:
            self.score-=5
        if(self.fever_cycle=='S'):
            self.score-=3
        elif(self.fever_cycle=='N'):
            self.score-=1
        elif(self.fever_cycle=='NN'):
            self.score+=5
        return self.score
            
    def sight_analyze(self,score):
        self.score=score
        if self.eye_sight=='Glasses':
            self.score-=2
        elif self.eye_sight=='Myopia' or self.eye_sight=='Hypermetropia':
            self.score-=3
        elif self.eye_sight=='Presbyopia':
            self.score-=5
        else:
            self.score+=5
        return self.score

    def __str__(self):
        return self.user.username 
    
    def save(self, *args, **kwargs):
            score=self.pulse_analyze()    
            score=self.bmi_analyze(score)      #saving the score
            score=self.whr_analyze(score)
            score=self.fever_calc(score)
            score=self.diab_analyze(score)
            score=self.sight_analyze(score)  
            super().save( *args, **kwargs)

class Doctor(models.Model):
    doctor_name=models.CharField(max_length=20)
    qualification=models.CharField(max_length=30)
    specialization=models.CharField(max_length=25,blank=True, default=None)
    phone_no=PhoneNumberField(blank=True,max_length=15)
    image=ImageField(default='default.jpg',upload_to='profile_pics')
    email=models.EmailField()
    document=models.URLField(max_length=200)
    postal_code=models.IntegerField(default=None,blank=True,null=True)
    def __str__(self):
        return self.doctor_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height> 300:
            outputsize = (300,300)
            img.thumbnail(outputsize)
            img.save(self.image.path)
