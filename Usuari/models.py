from django.db import models

# Create your models here.
class Usuari(models.Model):
    nom = models.TextField()
    adreca = models.TextField()
    telefon = models.IntegerField()
    esAdmin = models.BooleanField()

    def __unicode__(self):
        return self.nom