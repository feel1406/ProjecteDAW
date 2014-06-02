from django.conf.urls import patterns, url
from Blog import views

urlpatterns = patterns('',
                       
    url(r'^nouPost/', views.NouPost, name='nouPost'),
    
    url(r'^blog/', views.VeureBlog, name='blog'),

)