from django.db import models 
from django.contrib.auth.models import AbstractUser 

# Create your models here. 
class CustomerUser(AbstractUser):    
    user_photo = models.ImageField(blank=True) #default = "경로/사진.jpg" 지정하면 기본사진으로 됨 
    
    def __str(self):        
        return self.email