# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Weather(models.Model):
    basetime = models.DateTimeField()
    fcstTime = models.DateTimeField()
    temp = models.CharField(max_length=8)
    rain = models.IntegerField()