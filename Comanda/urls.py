from django.conf.urls import patterns, url
from Comanda import views

urlpatterns = patterns('',
                       
    url(r'^novaComanda/', views.NovaComanda, name='novaComanda'),
    
    url(r'^lesMevesComandes/', views.LesMevesComandes, name='lesMevesComandes'),

    url(r'^comandesClients/', views.ComandesClients, name='comandesClients'),
    
    url(r'^entradaProductes/', views.EntrarProducte, name='entradaProductes'),
    
    url(r'^consultaPizza/', views.ConsultaPizza, name='consultaPizza'),
    
    url(r'^consultaIngredient/', views.ConsultaIngredient, name='consultaIngredient'),
    
    url(r'^consultaTipusPizza/', views.ConsultaTipusPizza, name='consultaTipusPizza'),
    
    url(r'^obtenirComandes/', views.CopiaSeguretatComanda, name='obtenirComandes'),

)