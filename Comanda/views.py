from django.shortcuts import render

def NovaComanda(request):
    return render(request, 'Comanda/novaComanda.html')

def LesMevesComandes(request):
    return render(request, 'Comanda/lesMevesComandes.html')