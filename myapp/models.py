# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class Mapp(models.Model):
    camera_id = models.CharField(max_length=100, primary_key='True')
    light_id = models.CharField(max_length=100,unique='True')
    created_on = models.CharField(max_length=10)


class Crossing1(models.Model):
    cam = models.ForeignKey(Mapp)
    conclusion = models.CharField(max_length=30, default=None)
    stray = models.BooleanField(default=False)
