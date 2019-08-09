from django.db import models
from django.utils import timezone

class Question(models.Model):
    q_title = models.TextField(blank=True, null=True)
    q_content = models.TextField(blank=True, null=True)
    q_created = models.DateTimeField(auto_now_add=True)
    q_updated = models.DateTimeField(auto_now=True)
    q_photo = models.FileField(blank=True, null=True)
    author_username = models.TextField(blank=True, null=True)
    author_id = models.IntegerField(default=0, blank=True)
    cnt = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ['-q_created']

class Q_Comment(models.Model):
    author_username = models.TextField(blank=True)
    author_id = models.IntegerField(blank=True,default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,blank=True, null=True, related_name='q_comment_set')
    
    q_reply = models.TextField(max_length=200, blank=False)
    q_c_created = models.DateTimeField(auto_now_add=True)
    q_c_updated = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return self.c_name + ':' + self.text