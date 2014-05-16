# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuari(models.Model):
    nom = models.TextField(max_length = 100, blank = False)
    adreca = models.TextField(max_length = 150, blank = False)
    telefon = models.IntegerField(max_length = 12, blank = False)
    email = models.EmailField(blank = False)
    contrasenya = models.TextField(blank = False, max_length = 15)
    esAdmin = models.BooleanField()
    usuari = models.OneToOneField(User)

    def __unicode__(self):
        return self.nom