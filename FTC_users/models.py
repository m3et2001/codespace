from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from FTC_users.managers import ThreadManager
# Create your models here.

class UserSignup(models.Model):
    Username=models.CharField(max_length=50,default="",unique=True)
    Firstname=models.CharField(max_length=30,default="")
    Lastname=models.CharField(max_length=30,default="")
    #Phone = models.BigIntegerField(default=0)
    Email=models.EmailField(max_length=254,default="",unique=True)
    Gender=models.CharField(max_length=10,default="")
    DOB=models.DateField(null=True, blank=True)
    City=models.CharField(max_length=30,default="")
    State=models.CharField(max_length=30,default="")
    Region=models.CharField(max_length=30,default="")

class Profile(models.Model):
    user=models.CharField(max_length=30,unique=True)
    token=models.CharField(max_length=150)
    verify=models.BooleanField(default=False)

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Thread(TrackingModel):
    THREAD_TYPE = (
        ('personal', 'Personal'),
        ('group', 'Group')
    )

    name = models.CharField(max_length=50, null=True, blank=True)
    thread_type = models.CharField(max_length=15, choices=THREAD_TYPE, default='personal')
    users = models.ManyToManyField('auth.User')

    objects = ThreadManager()

    def __str__(self) -> str:
        if self.thread_type == 'personal' and self.users.count() == 2:
            return f'{self.users.first()} and {self.users.last()}'
        return f'{self.name}'

class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=False,auto_now=False)
    #updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'From <Thread - {self.thread}>'