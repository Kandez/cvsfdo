from django.urls import path
from .views import home, noticia, nueva, editarnoticia, borrarnoticia

noticias_patterns = ([
    path('', home.as_view(), name='home'),
    path('<int:pk>/<slug:slug>', noticia.as_view(), name='noticia'),
    path('formularionoticia/', nueva.as_view(), name='nuevanoticia'),
    path('editarnoticia/<int:pk>/', editarnoticia.as_view(), name='editarnoticia'),
    path('confirmarborrar/<int:pk>/', borrarnoticia.as_view(), name='borrarnoticia'),
],'noticias')