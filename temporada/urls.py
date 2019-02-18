from django.contrib import admin
from django.urls import path, include
from .views import listaclubs, club, crearclub, editarclub, borrarclub


temporada_patterns = ([
    path ('', listaclubs.as_view(), name='listaclubs'),
    path('<int:pk>/<slug:slug>', club.as_view(), name='club'),
    path('formularioclub/', crearclub.as_view(), name='crearclub'),
    path('editarclub/<int:pk>/', editarclub.as_view(), name='editarclub'),
    path('confirmarborrar/<int:pk>/', borrarclub.as_view(), name='borrarclub'),
    path('infoclub/<int:pk>/', club.as_view(), name="infoclub"),
], 'temporada')
