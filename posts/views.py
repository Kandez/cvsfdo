from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Repply
from .forms import PostForm, RepplyForm
from django.urls import reverse_lazy, reverse
# Create your views here.

class posts(ListView):
    model=Post

class post(DetailView):
    model=Post

class crearpost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/formulariopost.html'
    success_url = reverse_lazy('post:posts')

class editarpost(UpdateView):
    model = Post
    form_class= PostForm
    template_name = 'posts/editarpost.html'
    success_url = reverse_lazy('post:posts')

class borrarpost(DeleteView):
    model = Post
    template_name = 'posts/confirmarborrar.html'
    success_url = reverse_lazy('post:posts')


def crearrepply(request, post_id):
    form=RepplyForm(request.POST)
    post=Post.objects.get(pk=post_id)
    usuario=request.user
    respuesta=request.POST.get("contenido",'')
    repply=Repply(contenido=respuesta, usuario=usuario, post=post)
    repply.save()
    return render(request, "posts/formulariorepply.html", {'form': form, 'post':post})