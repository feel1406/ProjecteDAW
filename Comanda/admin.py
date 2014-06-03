from django.contrib import admin
from Comanda.models import Comanda, Ingredient, TipusPizza, LiniaComanda, Varietat

admin.site.register(TipusPizza)
admin.site.register(Ingredient)
admin.site.register(Comanda)
admin.site.register(LiniaComanda)
admin.site.register(Varietat)
