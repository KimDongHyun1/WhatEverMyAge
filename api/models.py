from django.db import models


class Pictures(models.Model):
    picture = models.FileField(upload_to='', blank=True)
    reply = models.TextField()

