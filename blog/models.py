from django.db import models
from django.utils import timezone
from users.models import CustomerUser

class Blog(models.Model):
    #pr = models.TextField(blank=True,unique=True,primary_key=True) 
    user = models.ForeignKey(CustomerUser, on_delete='CASCADE')
    like = models.IntegerField(default=0)
    title = models.TextField()
    content = models.TextField()
    photo = models.ImageField(blank=True) #default = "경로/사진.jpg" 지정하면 기본사진으로 됨
    gps = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

   # def __str__(self):
   #     return self.pk
    #like에 권한부여하기 읽기만하도록

    class Meta:
        ordering = ['-created']



class Comment(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete='CASCADE')
    blog = models.ForeignKey(Blog, on_delete='CASCADE')
    reply = models.TextField(max_length=200, blank=False)
    c_created = models.DateTimeField(auto_now_add=True)
    c_updated = models.DateTimeField(auto_now=True) 

#    def __str__(self):
#        return self.c_name + ':' + self.text

    class Meta:
        ordering = ['-c_created']
       
# 비밀번호  ,친구추가