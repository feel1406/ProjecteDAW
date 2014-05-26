from django.forms import ModelForm
from django import forms
from Comanda.models import TipusPizza

class AfegirPizza(forms.Form):
    class Meta:
        model = TipusPizza
        fields = ['nom_pizza', 'tipus_pizza', 'preu_base', 'es_predefinida', 'imatge_pizza_ext']
        widgets = {
                   'nom_pizza': forms.TextInput(attrs={'placeholder' : 'Nom De La Pizza', 'class' : 'form-control', 'type' : 'text'}),
                   'nom_pizza': forms.Select(attrs={'placeholder' : 'Tipus De Pizza', 'class' : 'form-control', 'type' : 'text'}),
                   'preu_base': forms.TextInput(attrs={'placeholder' : 'Preu Base', 'class' : 'form-control', 'type' : 'text'}),
                   'es_predefinida': forms.CheckboxInput(),
                   'imatge_pizza_ext': forms.TextInput(attrs={'placeholder' : 'Nom Fitxer Imatge', 'class' : 'form-control', 'type' : 'text'})
                   }