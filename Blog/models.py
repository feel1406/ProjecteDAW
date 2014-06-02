# -*- encoding: utf-8 -*-
from django.db import models
from Usuari.models import User

class Post(models.Model):
    
    TEMA_CHOICES = (
                     ('Ofertes', 'Ofertes'),
                     ('Novetats', 'Novetats'),
                     ('Noticies', 'Notícies'),
    )
    
    titol = models.TextField(max_length = 200)
    entrada = models.TextField()
    autor = models.ForeignKey(User)
    data_publicacio = models.DateField()
    tema = models.TextField(max_length = 50, choices = TEMA_CHOICES)

    def __unicode__(self):
        return self.titol
