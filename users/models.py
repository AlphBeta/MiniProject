from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user=OneToOneField(User,on_delete='CASCADE')
    name=models.CharField(max_length=20,default='User')
    image=ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height> 300:
            outputsize = (300,300)
            img.thumbnail(outputsize)
            img.save(self.image.path)