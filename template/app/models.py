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
    workTime = models.DateTimeField(default=now)
    lat = models.FloatField()
    lng = models.FloatField()