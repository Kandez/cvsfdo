from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrarse.html', {
        'form': form
})

@login_required()
def contacta(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cleaneddata=form.cleaned_data
            nombre=cleaneddata['nombre']
            mensaje=cleaneddata['mensaje']
            email=cleaneddata['email']
            mail=EmailMessage(nombre, mensaje, email, to=['roberto.leon.django@gmail.com'])
            mail.send()
            return HttpResponseRedirect('../')
    else:
        form=ContactForm()
    return render(request, 'contacta.html', {'form':form})