# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from messaging.models import MyDevice
from django.db import models

# Create your models here.

class Message(models.Model):
    sender =models.ForeignKey(MyDevice, on_delete=models.CASCADE, related_name='sender')
    receiver =models.ForeignKey(MyDevice, on_delete=models.CASCADE, related_name='receiver')
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)