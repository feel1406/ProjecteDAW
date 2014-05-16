from django.db import models


# Create your models here.
class Comanda(models.Model):
    num_comanda = models.IntegerField(blank = False)
    data_comanda = models.DateField(blank = False)
    
    
class Ingredient(models.Model):
    ingredient = models.TextField(max_length = 150, blank = False)
    stock = models.IntegerField(blank = False)
    
    def __unicode__(self):
        return self.ingredient
    
class Categoria(models.Model):
    nom_categoria = models.TextField(max_length = 100, blank = False)
    
    def __unicode__(self):
        return self.nom_categoria