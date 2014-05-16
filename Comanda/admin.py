from django.contrib import admin
from Comanda.models import Comanda, Ingredient, Categoria

admin.site.register(Categoria)
admin.site.register(Ingredient)
admin.site.register(Comanda)
