from django.shortcuts import render
from Comanda.models import TipusPizza, Ingredient, Varietat
from Comanda.forms import AfegirPizza
from django.contrib import messages

def NovaComanda(request):
    pizzes = Varietat.objects.all()
    tipus = TipusPizza.objects.all()
    return render(request, 'Comanda/novaComanda.html', {'pizzes' : pizzes, 'tipus' : tipus})

def LesMevesComandes(request):
    return render(request, 'Comanda/lesMevesComandes.html')

def ComandesClients(request):
    return render(request, 'Comanda/comandesClients.html')

def EntrarProducte(request):
    if request.method == 'POST':
        formulariNovaPizza = AfegirPizza()
        if formulariNovaPizza.is_valid():
            formulariNovaPizza.save()
            messages.add_message(request, messages.INFO, 'Pizza afegida correctament')
            return render('Comanda/entrarProducte.html')
    else:
        formulariNovaPizza = AfegirPizza()
    pizza = TipusPizza.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'Comanda/entrarProducte.html', {'pizza' : pizza, 'ingredients' : ingredients, 'formulariNovaPizza' : formulariNovaPizza })