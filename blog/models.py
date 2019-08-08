from django.db import models
from django.utils import timezone
from users.models import CustomerUser

class Posting(models.Model):
#    author = models.ForeignKey(CustomerUser, on_delete='CASCADE', blank=True, null=True)
    author_username = models.TextField(blank=True)
    author_id = models.IntegerField(default=0, blank=True)
    title = models.CharField(max_length=100, blank=True)
    like = models.IntegerField(default=0, blank=True)
    content = models.TextField(blank=True)
    photo = models.FileField(blank=True, null=True)
    lat = models.DecimalField(blank=True, max_digits=19, decimal_places=10, null=True)
    lng = models.DecimalField(blank=True, max_digits=19, decimal_places=10, null=True)
    cnt = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['-created']    



class Comment(models.Model):
    #author = models.ForeignKey(CustomerUser, on_delete='CASCADE',blank=True, null=True)
    author_username = models.TextField(blank=True)
    author_id = models.IntegerField(blank=True,default=0)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE,blank=True, null=True, related_name='comment_set')
    reply = models.TextField(max_length=200, blank=False)

# 비밀번호

class Like(models.Model):
    likeCnt = models.IntegerField(blank=True, default=1)
    userId = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='userId_set')
    postingId = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='postingId')