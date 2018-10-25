from django.shortcuts import render
from django.utils import timezone
from .models import Post, Perro
from .forms import PostForm
from django.shortcuts import redirect


def index(request):
    return render(request, 'blog/index.html',)

def galeria(request):
    perro = Perro.objects.all()
    context = {'perros':perro}
    return render(request, 'blog/galeria.html', context)

def new_perro(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'blog/addperro.html', {'form': form})

def formulario(request):
    return render(request, 'blog/formulario.html',)

# Create your views here.