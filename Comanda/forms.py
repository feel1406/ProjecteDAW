from django.forms import ModelForm
from django import forms
from Comanda.models import TipusPizza

class AfegirPizza(forms.Form):
    class Meta:
        model = TipusPizza
        fields = ['nom_pizza', 'preu_base', 'es_predefinida', 'extensio_fitxer']
        widgets = {
                   'nom_pizza': forms.TextInput(attrs={'placeholder' : 'Nom De La Pizza', 'class' : 'form-control'}),
                   'preu_base': forms.TextInput(attrs={'placeholder' : 'Preu Base', 'class' : 'form-control'}),
                   'es_predefinida': forms.CheckboxInput(),
                   'extensio_fitxer': forms.TextInput(attrs={'placeholder' : 'Nom Fitxer Imatge', 'class' : 'form-control'})
                   }