# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Comanda(models.Model):
    data_comanda = models.DateField(blank = False)
    hora_comanda = models.DateField(blank = False)
    import_comanda = models.IntegerField(blank = False)
    comanda_pagada = models.BooleanField(blank = False)
    comanda_entregada = models.BooleanField(blank = False)
    client = models.ForeignKey(User)
    
class Ingredient(models.Model):
    nom_ingredient = models.TextField(max_length = 150, blank = False)
    preu_ingredient = models.IntegerField(blank = False, null = True)
    stock = models.IntegerField(blank = False, null = True)
    extensio_imatge = models.CharField(blank = False, max_length = 100)
    
    def __unicode__(self):
        return self.nom_ingredient
    
class Varietat(models.Model):
    nom_pizza = models.TextField(max_length = 100, blank = False)
    preu_base = models.IntegerField(blank = False, null = True)
    es_predefinida = models.BooleanField(blank = False)
    imatge_pizza_ext = models.TextField(blank = False, max_length = 100)
    
    def __unicode__(self):
        return self.nom_pizza

class TipusPizza(models.Model):
    PIZZA_CHOICES = (
                     ('Calzone', 'Calzone'),
                     ('Normal', 'Normal'),
                     ('Massa Fina', 'Massa Fina'),
                     ('Focaccia', 'Focaccia'),
                     ('Panini', 'Panini'),
                     ('Massa De Pa', 'Massa De Pa'),
    )     
    tipus_pizza = models.TextField(max_length = 50, choices = PIZZA_CHOICES )
    preu_tipus = models.IntegerField(max_length = 20)
    
class LiniaComanda(models.Model):
    quantitat = models.IntegerField(blank = False)
    id_comanda = models.ForeignKey(Comanda)
    id_tipus = models.ForeignKey(TipusPizza)
    id_varietat = models.ForeignKey(Varietat)    
    id_ingredient = models.ManyToManyField(Ingredient)