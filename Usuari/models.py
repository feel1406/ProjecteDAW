# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Usuari(models.Model):
    adreca = models.TextField(max_length = 150, blank = True)
    telefon = models.IntegerField(max_length = 12, blank = True, null = True)
    usuari = models.OneToOneField(User)

def CrearPerfilClient(sender, instance, created, **kwargs):
    if created:
        Usuari.objects.create(usuari = instance)
        
post_save.connect(CrearPerfilClient, sender = User)