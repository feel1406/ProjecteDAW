# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Arrel de la web: /
    url(r'^$', 'Proyecto.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^Usuari/', include('Usuari.urls', namespace = 'Usuari')),

    url(r'^Comanda/', include('Comanda.urls', namespace = 'Comanda')),
    
)
