from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PerroForm
from django.utils import timezone
from .models import Post, Perros




def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/index.html', {'posts' : posts})

def index(request):
    return render(request, 'blog/index.html', {})

def galeria(request):
    perro = Perros.objects.all()
    context = {'perros':perro}
    return render(request, 'blog/galeria.html', context)

def formulario(request):
    return render(request, 'blog/formulario.html', {})


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'blog/index.html'


class SignInView(LoginView):
    template_name = 'blog/iniciar_sesion.html'
class SignOutView(LogoutView):
    pass

def new_perro(request):
    if request.method == "POST":
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('galeria')
    else:
        form = PerroForm()
    return render(request, 'blog/addperro.html', {'form': form})
# Create your views here.