from django.contrib import admin
from Comanda.models import Comanda, Ingredient, TipusPizza, IngredientEnPizza, DadesComanda

admin.site.register(TipusPizza)
admin.site.register(Ingredient)
admin.site.register(Comanda)
admin.site.register(IngredientEnPizza)
admin.site.register(DadesComanda)