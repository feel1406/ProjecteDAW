# -*- encoding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from Usuari.forms import NouUsuariForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Funció per crear un nou usuari "Client" de la pizzeria:
def NouClient(request):
    if request.method == 'POST':
        form = NouUsuariForm(request.POST)
        if form.is_valid():
            #Creo un usuari de Django:
            usuari = User()
            #Assigno a una variable els valors del formulari:
            nouUsuari = form.save(commit = False)
            #Els usuaris que es creen són clients, i no tenen permissos d'administració:
            nouUsuari.esAdmin = False
            #Assigno a l'usuari de Django els valors dels camps del formulari que necessito:
            usuari.username = nouUsuari.nom
            usuari.email = nouUsuari.email
            usuari.password = nouUsuari.contrasenya
            #Creo l'usuari de Django
            usuari.save()
            #Faig l'assossiació entre l'usuari de Django i l'usuari dels models:
            nouUsuari.usuari = usuari
            #Creo un nou usuari de l'aplicació:
            nouUsuari.save()
            messages.add_message(request, messages.SUCCESS, 'Has creat el teu usuari correctament')
            url_next = reverse('Usuari/perfilClient.html')
            return HttpResponseRedirect(url_next)
        else:
            messages.add_message(request, messages.ERROR, 'Error creant l\'usuari')
    else:
        form = NouUsuariForm()
        
    return render(request, 'Usuari/nouUsuari.html', {'form' : form})

def Sortir(request):
    logout(request)
    return render(request, 'index.html', {})