from django.contrib import admin
from Comanda.models import Comanda, Ingredient, TipusPizza, DadesComanda, Varietat

admin.site.register(TipusPizza)
admin.site.register(Ingredient)
admin.site.register(Comanda)
admin.site.register(DadesComanda)
admin.site.register(Varietat)
