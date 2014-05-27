from django.db import models

class Comanda(models.Model):
    num_comanda = models.IntegerField(blank = False)
    data_comanda = models.DateField(blank = False)
    hora_comanda = models.DateTimeField(blank = False)
    import_comanda = models.IntegerField(blank = False)
    comanda_pagada = models.BooleanField(blank = False)
    
    
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
    imatge_pizza_ext = models.CharField(blank = False, max_length = 100)
    
    def __unicode__(self):
        return self.nom_pizza

class TipusPizza(models.Model):
    PIZZA_CHOICES = (
                     ('Calzone', 'CA'),
                     ('Normal', 'NO'),
                     ('Massa Fina', 'MF'),
                     ('Focaccia', 'FO'),
                     ('Panini', 'PA'),
                     ('Massa De Pa', 'MP'),
    )     
    tipus_pizza = models.TextField(max_length = 50, choices = PIZZA_CHOICES )
    preu_tipus = models.IntegerField(max_length = 20)
    
class VarietatPizzes(models.Model):
    varietat_pizza = models.ManyToManyField(Varietat)
    tipus = models.ManyToManyField(TipusPizza)
    
class IngredientEnPizza(models.Model):
    id_tipus_pizza = models.ForeignKey(TipusPizza)
    id_ingredient_pizza = models.ForeignKey(Ingredient)
    
class DadesComanda(models.Model):
    quantitat = models.IntegerField(blank = False)
    id_pizza_comanda = models.ForeignKey(TipusPizza)
    id_comanda_pizza = models.ForeignKey(Comanda)
    id_ingredient_pizza_comanda = models.ManyToManyField(Ingredient)