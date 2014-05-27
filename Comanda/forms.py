# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Comanda.models import Varietat, Ingredient

class AfegirPizza(ModelForm):
    class Meta:
        model = Varietat
        widgets = {
                   'nom_pizza': forms.TextInput(attrs={'placeholder' : 'Nom De La Pizza', 'class' : 'form-control', 'type' : 'text'}),
                   'preu_base': forms.TextInput(attrs={'placeholder' : 'Preu Base', 'class' : 'form-control', 'type' : 'text'}),
                   'es_predefinida': forms.CheckboxInput(),
                   'imatge_pizza_ext': forms.TextInput(attrs={'placeholder' : 'Extensió Fitxer', 'class' : 'form-control', 'type' : 'text'})
                   }
        fields = ['nom_pizza', 'preu_base', 'es_predefinida', 'imatge_pizza_ext']
        
class AfegirIngredient(ModelForm):
    class Meta:
        model = Ingredient
        widgets = {
                   'nom_ingredient': forms.TextInput(attrs={'placeholder' : 'Ingredient', 'class' : 'form-control', 'type' : 'text'}),
                   'preu_ingredient': forms.TextInput(attrs={'placeholder' : 'Preu', 'class' : 'form-control', 'type' : 'text'}),
                   'stock': forms.TextInput(attrs={'placeholder' : 'Unitats', 'class' : 'form-control', 'type' : 'text'}),
                   'extensio_imatge': forms.TextInput(attrs={'placeholder' : 'Extensió Fitxer', 'class' : 'form-control', 'type' : 'text'})
                   }
        fields = ['nom_ingredient', 'preu_ingredient', 'stock', 'extensio_imatge']