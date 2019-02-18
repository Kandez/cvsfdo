from django.contrib import admin
from .models import Jugador, Presidente, Club, Equipo, Entrenador, es_formado

# Register your models here.
admin.site.register(Club)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Entrenador)
admin.site.register(es_formado)
admin.site.register(Presidente)