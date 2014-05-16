# -*- encoding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from Usuari.forms import NouUsuariForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Funció per crear un nou usuari "Client" de la pizzeria:
def NouClient(request):
    if request.method == 'POST':
        form = NouUsuariForm(request.POST)
        if form.is_valid():
            usuari = User()
            nouUsuari = form.save(commit = False)
            nouUsuari.esAdmin = False
            usuari.username = nouUsuari.nom
            usuari.email = nouUsuari.email
            usuari.password = nouUsuari.contrasenya
            usuari.save()
            nouUsuari.usuari = usuari
            nouUsuari.save()
            messages.add_message(request, messages.SUCCESS, 'Has creat el teu usuari correctament')
            url_next = reverse('usuaris:perfilUsuari')
            return HttpResponseRedirect(url_next)
        else:
            messages.add_message(request, messages.ERROR, 'Error creant l\'usuari')
    else:
        form = NouUsuariForm()
        
    return render(request, 'Usuari/nouUsuari.html', {'form' : form})