from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):

    email = models.EmailField(blank=True,null=True)
    user_photo = models.FileField(blank=True) #default = "경로/사진.jpg" 지정하면 기본사진으로 됨