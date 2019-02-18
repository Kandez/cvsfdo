from django.contrib import admin
from .models import Noticia
# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'contenido', 'imagen')
    ordering = ('titulo', 'created')
    search_fields = ('titulo',)
    date_hierarchy = 'created'

admin.site.register(Noticia, NoticiaAdmin)
