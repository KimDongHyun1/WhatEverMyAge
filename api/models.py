from django.db import models

class Pictures(models.Model):
    picture = models.ImageField(null=True, default=None, blank=True)
    description = models.TextField()

class Post(models.Model):
    message = models.TextField()
    title = models.TextField()