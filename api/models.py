from django.db import models

class Pictures(models.Model):
    picture = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)
    #picture = models.ImageField(null=True, default=None, blank=True)

class Post(models.Model):
    message = models.TextField()
    title = models.TextField()