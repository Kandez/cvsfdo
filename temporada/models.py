from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Presidente(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre Presidente")
    appresidente=models.CharField(max_length=50, verbose_name="Apellido Presidente")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Presitente"
        verbose_name_plural="Presidentes"
        ordering=["-created"]

    def __str__(self):
        return str(self.nombre+" "+self.appresidente)

class Club(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre Club")
    imagen=models.ImageField(verbose_name="Imagen", upload_to='temporada', null=True, blank=True)
    descripcion=models.CharField(max_length=20000, verbose_name="Descripcion Club")
    id_presidente=models.OneToOneField(Presidente, on_delete=models.CASCADE, null=True, blank=True)
    fundado=models.CharField(max_length=50, verbose_name="Año de fundacion")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Club"
        verbose_name_plural="Clubes"
        ordering=["-created"]

    def __str__(self):
        return str(self.nombre)

class Jugador(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre Jugador")
    ap1jugador=models.CharField(max_length=50, verbose_name="Apellido1 Jugador")
    ap2jugador=models.CharField(max_length=50, verbose_name="Apellido2 Jugador")
    edad=models.IntegerField(verbose_name="Edad Jugador")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Jugador"
        verbose_name_plural="Jugadores"
        ordering=["-created"]

    def __str__(self):
        return str(self.nombre+" "+self.ap1jugador+" "+self.ap2jugador)

class Equipo(models.Model):
    categoria=models.CharField(max_length=50, verbose_name="Categoria equipo")
    id_club=models.ForeignKey(Club, verbose_name="Id Club", on_delete=models.CASCADE)
    jugador=models.ManyToManyField(Jugador, through="es_formado")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Equipo"
        verbose_name_plural="Equipos"
        ordering=["-created"]

    def __str__(self):
        return str(self.id_club)+" "+str(self.categoria)


class Entrenador(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre entrenador")
    ap1entrenador=models.CharField(max_length=50, verbose_name="Apellido1 entrenador")
    ap2entrenador=models.CharField(max_length=50, verbose_name="Apellido2 entrenador")
    edad=models.IntegerField(verbose_name="Edad entrenador")
    id_equipo=models.ForeignKey(Equipo, verbose_name="Id Equipo", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Entrenador"
        verbose_name_plural="Entrenadores"
        ordering=["-created"]

    def __str__(self):
        return str(self.nombre+" "+self.ap1entrenador+" "+self.ap1entrenador)+" "+str(self.id_equipo)

class es_formado(models.Model):
    id_equipo=models.ForeignKey(Jugador, on_delete=models.CASCADE)
    id_jugador=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Desc Equipo"
        verbose_name_plural="Desc Equipo"
        ordering=["-created"]

    def __str__(self):
        return str(self.id_equipo)+" "+str(self.id_jugador)