# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pets(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

