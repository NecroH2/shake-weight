from django.urls import path
from . import views
from blog.views import SignUpView, BienvenidaView, SignInView, SignOutView
from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario'),
    path('addperro', views.new_perro, name='addperro'),

    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
]

