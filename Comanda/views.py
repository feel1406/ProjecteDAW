# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Comanda.models import TipusPizza, Ingredient, Varietat
from Comanda.forms import AfegirPizza, AfegirIngredient
from django.contrib import messages

def NovaComanda(request):
    pizzes = Varietat.objects.all()
    tipus = TipusPizza.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'Comanda/novaComanda.html', {'pizzes' : pizzes, 'tipus' : tipus, 'ingredients' : ingredients})

def LesMevesComandes(request):
    return render(request, 'Comanda/lesMevesComandes.html')

def ComandesClients(request):
    return render(request, 'Comanda/comandesClients.html')

def EntrarProducte(request):
    if request.method == 'POST':
        formulariNovaPizza = AfegirPizza(request.POST)
        formulariNouIngredient = AfegirIngredient(request.POST)
        if formulariNovaPizza.is_valid():
            formulariNovaPizza.save()
            messages.add_message(request, messages.INFO, 'Pizza afegida correctament')
            url_next = reverse('Comanda:entradaProductes')
            return HttpResponseRedirect(url_next)
        if formulariNouIngredient.is_valid:
            formulariNouIngredient.save()
            messages.add_message(request, messages.INFO, 'Ingredient afegit correctament')
            url_next = reverse('Comanda:entradaProductes')
            return HttpResponseRedirect(url_next)
    else:
        formulariNovaPizza = AfegirPizza()
        formulariNouIngredient = AfegirIngredient()
    pizza = Varietat.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'Comanda/entrarProducte.html', { 'pizza' : pizza, 'ingredients' : ingredients, 'formulariNovaPizza' : formulariNovaPizza, 'formulariNouIngredient' : formulariNouIngredient })
