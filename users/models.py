from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField


# Create your models here.
class Profile(models.Model):
    user=OneToOneField(User,on_delete='CASCADE')
    image=ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return self.user.username