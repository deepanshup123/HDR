from django.db import models

# Create your models here.

class User_Register(models.Model):
    username = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    confirm_password = models.CharField(max_length = 100)

    def __str__(self):
        return self.username