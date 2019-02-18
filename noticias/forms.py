from django import forms
from .models import Noticia
import datetime

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo', 'imagen', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
        }