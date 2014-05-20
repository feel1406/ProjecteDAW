from django.shortcuts import render

def NovaComanda(request):
    return render(request, 'Comanda/novaComanda.html')

def LesMevesComandes(request):
    return render(request, 'Comanda/lesMevesComandes.html')

def ComandesClients(request):
    return render(request, 'Comanda/comandesClients.html')

def EntrarProducte(request):
    return render(request, 'Comanda/entrarProducte.html')