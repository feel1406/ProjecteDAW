from django.conf.urls import patterns, url
from Usuari import views

urlpatterns = patterns('',
                       
    url(r'^nouClient/', views.NouClient, name='nouClient')

)