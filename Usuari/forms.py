# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Usuari.models import Usuari

class NouUsuariForm(ModelForm):
    class Meta:
        model = Usuari
        widgets = {
                   'nom': forms.TextInput(attrs={'placeholder' : 'Nom', 'class' : 'form-control'}),
                   'adreca': forms.TextInput(attrs={'placeholder' : 'Adreça', 'class' : 'form-control'}),
                   'telefon': forms.TextInput(attrs={'placeholder' : 'Telèfon De Contacte', 'class' : 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder' : 'Email', 'class' : 'form-control', 'type': 'email'}),
                   'contrasenya': forms.TextInput(attrs={'placeholder' : 'Contrasenya', 'class' : 'form-control', 'type' : 'password'}),}
        fields = ['nom', 'adreca', 'telefon', 'email', 'contrasenya']