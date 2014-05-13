from django.db import models


# Create your models here.
class Comanda(models.Model):
    num_comanda = models.IntegerField()
    data_comanda = models.DateField()
    
    
class Ingredient(models.Model):
    ingredient = models.TextField()