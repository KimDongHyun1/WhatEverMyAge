from django.db import models

class Pictures(models.Model):
    picture = models.ImageField(null=True, default=None, blank=True)
