# -*- encoding: utf-8 -*-
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def QuiSom(request):
    return render(request, 'quiSom.html')

def Contacte(request):
    return render(request, 'contacte.html')

def OnSom(request):
    return render(request, 'onSom.html')

def TreballaAmbNosaltres(request):
    return render(request, 'treballaAmbNosaltres.html')