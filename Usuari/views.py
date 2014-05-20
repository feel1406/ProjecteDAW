# -*- encoding: utf-8 -*- 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from Usuari.forms import NouUsuariForm, DadesUsuari, LoginForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from Usuari.models import Usuari
from django.contrib.auth import logout, login, authenticate

# Funció per crear un nou usuari "Client" de la pizzeria:
def NouClient(request):
    if request.method == 'POST':
        form = NouUsuariForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            email = form.cleaned_data['email']
            usuari = User.objects.create_user(user, email, passwd)
            usuari.save()
            user = authenticate(username = user, password = passwd)
            if user is not None:
                login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Has creat el teu usuari correctament')
            return render(request, 'Usuari/perfilUsuari.html')
        else:
            messages.add_message(request, messages.ERROR, 'Error creant l\'usuari')
    else:
        form = NouUsuariForm()
        
    return render(request, 'Usuari/nouUsuari.html', { 'form' : form })

@login_required
def DadesClient(request):
    if request.method == 'POST':
        formulariDades = DadesUsuari(request.POST)
        if formulariDades.is_valid():
            usuari = Usuari()
            formulariDades.save(commit = False)
            usuari.adreca = formulariDades.adreca
            usuari.telefon = formulariDades.telefon
            formulariDades.save()
            messages.add_message(request, messages.SUCCESS, 'Dades de contacte desades correctament')
            url_next = reverse('Usuari/perfilUsuari.html')
            return HttpResponseRedirect(url_next)
        else:
            messages.add_message(request, messages.ERROR, 'Hi ha hagut un error. Intenta-ho una nova vegada')
    else:
        formulariDades = DadesUsuari()
        
    return render(request, 'Usuari/dadesClient.html', {'formulariDades' : formulariDades})

@login_required    
def PerfilClient(request):
    return render(request, 'Usuari/perfilUsuari.html')    

def Accedir(request):
    if request.method == 'POST':
        formulariLogin = LoginForm(request.POST)
        if formulariLogin.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                messages.add_message(request, messages.ERROR, 'Usuari i/o Contrasenya incorrectes..')
    else:
        formulariLogin = LoginForm()
    return render(request, 'Usuari/accedir.html', {'formulariLogin': formulariLogin})
    
def Sortir(request):
    logout(request)
    return HttpResponseRedirect('/')
