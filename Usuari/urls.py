from django.conf.urls import patterns, url
from Usuari import views

urlpatterns = patterns('',
                       
    url(r'^nouClient/', views.NouClient, name='nouClient'),
    
    url(r'^dadesClient/', views.DadesClient, name='dadesClient'),
    
    url(r'^perfilClient/', views.PerfilClient, name='perfilClient'),
    
    url(r'^accedir/', views.Accedir, name='accedir'),
    
    url(r'^sortir/', views.Sortir, name = "sortir"),

)