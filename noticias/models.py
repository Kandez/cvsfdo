from django.db import models
# Create your models here.

class Noticia(models.Model):
    titulo=models.CharField(max_length=50, verbose_name="Titulo")
    imagen=models.ImageField(verbose_name="Imagen", upload_to='noticias', null=True, blank=True)
    contenido=models.CharField(max_length=20000, verbose_name="Contenido noticia")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Noticia"
        verbose_name_plural="Noticias"
        ordering=["-created"]

    def __str__(self):
        return str(self.titulo)