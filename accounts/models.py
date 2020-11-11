from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
     status=models.CharField(max_length=10,default='Active')
     phone=models.CharField(max_length=10,blank=True,null=True)
     location=models.CharField(max_length=100,blank=True,null=True)
     profile=models.ImageField(upload_to="images/users",blank=True,null=True,default='images/users/default/brand.png')
    

     def __str__(self):
         return f'{self.user}'
