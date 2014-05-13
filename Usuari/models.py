from django.db import models

# Create your models here.
class Usuari(models.Model):
    nom = models.TextField(max_length = 100)
    adreca = models.TextField(max_length = 150)
    telefon = models.IntegerField()
    esAdmin = models.BooleanField()

    def __unicode__(self):
        return self.nom