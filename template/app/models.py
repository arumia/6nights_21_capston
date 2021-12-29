# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Weather(models.Model):
    basetime = models.DateTimeField()
    fcstTime = models.DateTimeField()
    temp = models.CharField(max_length=8)
    rain = models.IntegerField()

class Work(models.Model):
    uid = models.CharField(max_length=20)
    workTime = models.DateTimeField(default=now)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    crop = models.TextField(null=True)
    year = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    recent = models.TextField(null=True)
    others = models.TextField(null=True)