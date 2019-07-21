from django.db import models
from django.utils import timezone

class Question(models.Model):
    #user
    #pr = models.TextField(blank=True,unique=True,primary_key=True) 
    q_title = models.TextField()
    q_content = models.TextField()
    q_created = models.DateTimeField(auto_now_add=True)
    q_updated = models.DateTimeField(auto_now=True)

   # def __str__(self):
   #     return self.pk

    class Meta:
        ordering = ['-q_created']

class Q_Comment(models.Model):
    question = models.ForeignKey(Question, on_delete='CASCADE')
    q_reply = models.TextField(max_length=200, blank=False)
    q_c_created = models.DateTimeField(auto_now_add=True)
    q_c_updated = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return self.c_name + ':' + self.text