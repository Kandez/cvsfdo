from django import forms

class ContactForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    mensaje=forms.CharField(widget=forms.Textarea)
