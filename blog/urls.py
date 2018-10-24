from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario'),
]

