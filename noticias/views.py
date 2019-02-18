from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia
from django.urls import reverse_lazy, reverse
from .forms import NoticiaForm
# Create your views here.

class home(ListView):
    model = Noticia
    template_name = 'noticias/home.html'

class noticia(DetailView):
    model = Noticia
    template_name = 'noticias/noticia.html'

class nueva(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/formularionoticia.html'
    success_url = reverse_lazy('noticias:home')

class editarnoticia(UpdateView):
    model = Noticia
    fields = ['titulo', 'imagen', 'contenido']
    template_name = 'noticias/editarnoticia.html'
    success_url = reverse_lazy('noticias:home')

class borrarnoticia(DeleteView):
    model = Noticia
    template_name = 'noticias/confirmarborrar.html'
    success_url = reverse_lazy('noticias:home')