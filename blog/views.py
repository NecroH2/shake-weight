from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/index.html', {'posts' : posts})

def index(request):
    return render(request, 'blog/index.html',)

def galeria(request):
    return render(request, 'blog/galeria.html',)

def formulario(request):
    return render(request, 'blog/formulario.html',)
# Create your views here.