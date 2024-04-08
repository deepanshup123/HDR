from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserVerification(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 16)
    otp = models.IntegerField()
    status = models.BooleanField(default = False)
class Video_Add(models.Model):
    title = models.CharField(max_length = 200)
    video = models.FileField(upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class Job_profile(models.Model):
    full_name = models.CharField(max_length = 100)
    mobile_no = models.BigIntegerField()
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    skill = models.CharField(max_length=50)
    experience  = models.FloatField()
    image = models.ImageField(upload_to='Images/')
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.full_name
    

class Remembers(models.Model):
    full_name = models.CharField(max_length = 100)
    city = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/')
    experience  = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class ForgetPassword(models.Model):
    email = models.EmailField()
    otp = models.IntegerField()