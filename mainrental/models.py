from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mainrental_rs(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)

class mainrental_register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20,null=True,blank=True)

class bookingdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    price=models.CharField(max_length=50,null=True,blank=True)
    hours=models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    start_date_time=models.CharField(max_length=20,null=True,blank=True)
    end_date_time=models.CharField(max_length=20,null=True,blank=True)
    car=models.ForeignKey(mainrental_rs,on_delete=models.CASCADE)
