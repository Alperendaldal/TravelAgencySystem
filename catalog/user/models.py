from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

# Create your models here.



class Customer_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Tel_No = models.CharField(max_length=10,verbose_name='Phone Number',null=True,default='Add İnfo')
    Emergency_Number = models.CharField(max_length=10,null=True,default='Add İnfo')
    Birthday = models.DateField(verbose_name='Birthday',null=True,default='1900-01-01')
    Gender = models.CharField(max_length=10,verbose_name='Gender',null=True,default='Add İnfo')

    def id(self):
        return self.id