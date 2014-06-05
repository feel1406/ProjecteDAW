# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from Blog.models import Post
from django import forms

class NouPostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
                   'titol': forms.TextInput(attrs={'placeholder' : 'Títol', 'class' : 'form-control', 'type' : 'text'}),
                   'entrada': forms.Textarea(attrs={'placeholder' : 'Escriu aquí la noticia...', 'class' : 'form-control', 'type' : 'text'}),
                   'tema': forms.Select(attrs={'placeholder' : 'Tema', 'class' : 'form-control', 'type' : 'text'}),
                   }
        fields = ['titol', 'entrada', 'tema']