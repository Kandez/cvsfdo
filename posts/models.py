from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo=models.CharField(max_length=50, verbose_name="titulo")
    descripcion=models.CharField(max_length=1000, verbose_name="descripcion")
    imagen=models.ImageField(verbose_name="imagen", upload_to='posts', null=True, blank=True)
    archivo=models.FileField(verbose_name="archivo", upload_to='posts', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"
        ordering=["-created"]

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    usuario=models.OneToOneField(User, verbose_name="id usuario", on_delete=models.CASCADE)
    nombre=models.CharField(max_length=20, verbose_name="nombre")
    fnac=models.DateField(verbose_name="fecha nacimiento")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Repply(models.Model):
    contenido=models.CharField(verbose_name="contenido", max_length=1000)
    usuario=models.ForeignKey(User, verbose_name="id usuario", on_delete=models.CASCADE)
    post=models.ForeignKey(Post, verbose_name="id post", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Repply"
        verbose_name_plural="Repplies"
        ordering=["-created"]

    def __str__(self):
        return self.contenido