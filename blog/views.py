from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Perro


def index(request):
    return render(request, 'blog/index.html',)

def galeria(request):
    perro = Perro.objects.all()
    context = {'perros':perro}
    return render(request, 'blog/galeria.html', context)

def formulario(request):
    return render(request, 'blog/formulario.html',)

def addperro(request):
    return render(request, 'blog/addperro.html',)
# Create your views here.