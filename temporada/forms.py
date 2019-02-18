from django import forms
from .models import Club
import datetime

class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ['nombre', 'imagen', 'descripcion', 'fundado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fundado': forms.TextInput(attrs={'class':'form-control'}),
        }   
