# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Arrel de la web: 
    url(r'^$', 'Proyecto.views.Index', name='Index'),
    # Link d'administració del lloc:
    url(r'^admin/', include(admin.site.urls)),
    # URL de l'Usuari:
    url(r'^Usuari/', include('Usuari.urls', namespace = 'Usuari')),
    # URL de les Comandes:
    url(r'^Comanda/', include('Comanda.urls', namespace = 'Comanda')),
    
    url(r'^QuiSom/$', 'Proyecto.views.QuiSom', name='QuiSom'),
    
    url(r'^Contacte/$', 'Proyecto.views.Contacte', name='Contacte'),
    
    url(r'^OnSom/$', 'Proyecto.views.OnSom', name='OnSom'),
    
    url(r'^Treball/$', 'Proyecto.views.TreballaAmbNosaltres', name='TreballaAmbNosaltres'),
        
)
