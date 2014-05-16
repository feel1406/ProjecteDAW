from django.shortcuts import render

def NovaComanda(request):
    return render('novaComanda.html')

def LesMevesComandes(request):
    return render('lesMevesComandes.html')