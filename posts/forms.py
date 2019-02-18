from django import forms
from .models import Post, Repply
import datetime

class PostForm(forms.ModelForm):

    class Meta:
        model =Post
        fields = ['titulo', 'descripcion', 'imagen', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }   
        
class RepplyForm(forms.Form):

    contenido=forms.CharField(label="contenido", max_length=10000, required=True)
