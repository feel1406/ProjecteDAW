# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Comanda.models import TipusPizza, Ingredient, Varietat, Comanda, VarietatPizzes, IngredientEnPizza, DadesComanda
from Comanda.forms import AfegirPizza, AfegirIngredient
from django.contrib import messages
import json
import datetime


def NovaComanda(request):
    data = datetime.datetime.now()
    pizzes = Varietat.objects.all()
    tipus = TipusPizza.objects.all()
    ingredients = Ingredient.objects.all()
    c = Comanda()
    c.comanda_pagada = False
    c.data_comanda = data
    return render(request, 'Comanda/novaComanda.html', {'pizzes' : pizzes, 'tipus' : tipus, 'ingredients' : ingredients})

def ConsultaPizza(request):
    pizza = request.GET.get('nom_pizza')
    varietat = Varietat.objects.get(nom_pizza = pizza)
    respostaAjax = dict()
    respostaAjax['nomFitxer'] = varietat.imatge_pizza_ext
    respostaAjax['nomPizza'] = varietat.nom_pizza
    respostaAjax['preu'] = varietat.preu_base
    return HttpResponse(json.dumps(respostaAjax), content_type = 'application/json')

def ConsultaIngredient(request):
    ingredientSeleccionat = request.GET.get('nom_ingredient')
    ingredient = Ingredient.objects.get(nom_ingredient = ingredientSeleccionat)
    print ingredient.preu_ingredient
    respostaAjaxIng = dict()
    respostaAjaxIng['extFitxer'] = ingredient.extensio_imatge
    respostaAjaxIng['nomIngredient'] = ingredient.nom_ingredient
    respostaAjaxIng['preuIngredient'] = ingredient.preu_ingredient
    return HttpResponse(json.dumps(respostaAjaxIng), content_type = 'application/json')

def ConsultaTipusPizza(request):
    tipusSeleccionat = request.GET.get('tipus_pizza')
    tipus = TipusPizza.objects.get(tipus_pizza = tipusSeleccionat)
    respostaAjaxTipus = dict()
    respostaAjaxTipus['tipus'] = tipus.tipus_pizza
    respostaAjaxTipus['preu'] = tipus.preu_tipus
    return HttpResponse(json.dumps(respostaAjaxTipus), content_type = 'application/json')

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
