from django.db import models
from django.utils import timezone
from users.models import CustomerUser

class Posting(models.Model):
    author = models.ForeignKey(CustomerUser, on_delete='CASCADE', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True)
    like = models.IntegerField(default=0, blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(null=True, default=None, blank=True) #default = "경로/사진.jpg" 지정하면 기본사진으로 됨
    gps1 = models.DecimalField(blank=True, max_digits=19, decimal_places=10,default=0.0)
    gps2 = models.DecimalField(blank=True, max_digits=19, decimal_places=10,default=0.0)
    cnt = models.IntegerField(default=0, blank=True)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)    

  # def __str__(self):
  #     return self.pk
    #like에 권한부여하기 읽기만하도록

#    class Meta:
#        ordering = ['-created']



class Comment(models.Model):
    author = models.ForeignKey(CustomerUser, on_delete='CASCADE',blank=True, null=True)
    posting = models.ForeignKey(Posting, on_delete='CASCADE',blank=True, null=True)
    reply = models.TextField(max_length=200, blank=False)
#    c_created = models.DateTimeField(auto_now_add=True)
#    c_updated = models.DateTimeField(auto_now=True) 

#    def __str__(self):
#        return self.c_name + ':' + self.text

#    class Meta:
#        ordering = ['-c_created']
       
# 비밀번호  ,친구추가