# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuari(models.Model):
    nom = models.TextField(max_length = 100, blank = False, help_text = "Nom")
    adreca = models.TextField(max_length = 150, blank = False, help_text = "Adreça")
    telefon = models.IntegerField(max_length = 12, blank = False, help_text = "Telèfon")
    esAdmin = models.BooleanField()
    usuari = models.OneToOneField(User)

    def __unicode__(self):
        return self.nom