from django.conf.urls import patterns, url
from Comanda import views

urlpatterns = patterns('',
                       
    url(r'^novaComanda/', views.NovaComanda, name='novaComanda'),
    
    url(r'^lesMevesComandes/', views.LesMevesComandes, name='lesMevesComandes')

)