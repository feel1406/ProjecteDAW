from django.db import models

class Comanda(models.Model):
    num_comanda = models.IntegerField(blank = False)
    data_comanda = models.DateField(blank = False)
    hora_comanda = models.DateTimeField(blank = False)
    import_comanda = models.IntegerField(blank = False)
    
    
class Ingredient(models.Model):
    nom_ingredient = models.TextField(max_length = 150, blank = False)
    preu_ingredient = models.IntegerField(blank = False)
    stock = models.IntegerField(blank = False)
    extensio_imatge = models.CharField(blank = False)
    
    
    def __unicode__(self):
        return self.ingredient
    
class TipusPizza(models.Model):
    nom_pizza = models.TextField(max_length = 100, blank = False)
    preu_base = models.IntegerField(blank = False)
    
    def __unicode__(self):
        return self.nom_categoria
    
class IngredientEnPizza(models.Model):
    id_tipus_pizza = models.ManyToOneRel(TipusPizza)
    id_ingredient_pizza = models.ManyToOneRel(Ingredient)
    
class DadesComanda(models.Model):
    id_pizza_comanda = models.ManyToOneRel(TipusPizza)
    id_comanda_pizza = models.ManyToOneRel(Comanda)
    id_ingredient_pizza_comanda = models.ManyToOneRel(Ingredient)