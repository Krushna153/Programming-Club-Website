from django.db import models

# Create your models here.

class Announcement(models.Model):
    
    title = models.CharField(max_length=1000)
    # title_description = models.CharField(max_length=1000)
    #date_time = models.DateTimeField()
    # img = models.ImageField(upload_to='pics',blank=True, null=True)

    objects = models.Manager()

class Event(models.Model):
    
    title = models.CharField(max_length=1000)
    title_description = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pics',blank=True, null=True)
    date_time = models.DateTimeField()

    objects = models.Manager()

class Resource(models.Model):
    
    # title = models.CharField(max_length=100)
    resource = models.URLField(max_length = 100) 
    url_title = models.CharField(max_length = 500)
    tags = models.CharField(max_length=500)
    # img = models.ImageField(upload_to='pics',blank=True, null=True)
    # title_description = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='pics',blank=True, null=True)
    # date_time = models.DateTimeField()

    objects = models.Manager()
    #filefield