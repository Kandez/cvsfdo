from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Club
from django.urls import reverse_lazy, reverse
from .forms import ClubForm
# Create your views here.

class listaclubs(ListView):
    model = Club

class club(DetailView):
    model = Club

class crearclub(CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'temporada/formularioclub.html'
    success_url = reverse_lazy('temporada:listaclubs')

class editarclub(UpdateView):
    model = Club
    fields = ['nombre', 'imagen', 'descripcion', 'fundado']
    template_name = 'temporada/editarclub.html'
    success_url = reverse_lazy('temporada:listaclubs')

class borrarclub(DeleteView):
    model = Club
    template_name = 'temporada/confirmarborrar.html'
    success_url = reverse_lazy('temporada:listaclubs')