# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuari(models.Model):
    adreca = models.TextField(max_length = 150, blank = False)
    telefon = models.IntegerField(max_length = 12, blank = False)
    usuari = models.OneToOneField(User)
