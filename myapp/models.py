from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPES = (
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    )
    link = models.URLField(max_length=200)
    work_type = models.CharField(max_length=2, choices=WORK_TYPES)
