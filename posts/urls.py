from django.contrib import admin
from django.urls import path, include
from . import views
from .views import posts, post, crearpost, editarpost, borrarpost, crearrepply

post_patterns = ([
    path('', posts.as_view(), name="posts"),
    path('<int:pk>/<slug:slug>', post.as_view(), name='post'),
    path('formulariopost/', crearpost.as_view(), name='crearpost'),
    path('editarpost/<int:pk>/', editarpost.as_view(), name='editarpost'),
    path('confirmarborrar/<int:pk>/', borrarpost.as_view(), name='borrarpost'),
    path('formulariorepply/<int:post_id>/', views.crearrepply, name="crearrepply"),
], 'post')