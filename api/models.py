from django.db import models


class Pictures(models.Model):
    picture = models.FileField(upload_to='')
    #picture = models.ImageField(null=True, default=None, blank=True)


class Post(models.Model):
    message = models.TextField()
    title = models.TextField()