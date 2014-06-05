# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from Usuari.models import Usuari

class NouUsuariForm(ModelForm):
    class Meta:
        model = User
        widgets = {
                   'username': forms.TextInput(attrs={'placeholder' : 'Nom', 'class' : 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder' : 'Email', 'class' : 'form-control', 'type': 'email'}),
                   'password': forms.TextInput(attrs={'placeholder' : 'Contrasenya', 'class' : 'form-control', 'type' : 'password'}),}
        fields = ['username', 'email', 'password']
        
        
class DadesUsuari(ModelForm):
    class Meta:
        model = Usuari
        widgets = {
                   'adreca': forms.TextInput(attrs={'placeholder' : 'Adreça', 'class' : 'form-control', 'id' : 'adreca'}),
                   'telefon': forms.TextInput(attrs={'placeholder' : 'Telèfon', 'class' : 'form-control', 'id' : 'telefon'}),
                   }
        fields = [ 'adreca', 'telefon']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder':'Nom d\'Usuari', 'type' : 'text', 'class': 'form-control'}))
    password = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder':'Contrasenya', 'type' : 'password', 'class': 'form-control'}))