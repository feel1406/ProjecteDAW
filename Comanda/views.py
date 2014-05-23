from django.shortcuts import render
from Comanda.models import TipusPizza, Ingredient

def NovaComanda(request):
    return render(request, 'Comanda/novaComanda.html')

def LesMevesComandes(request):
    return render(request, 'Comanda/lesMevesComandes.html')

def ComandesClients(request):
    return render(request, 'Comanda/comandesClients.html')

def EntrarProducte(request):
    pizza = TipusPizza.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'Comanda/entrarProducte.html', {'pizza' : pizza, 'ingredients' : ingredients})