from django.contrib import admin
from .models import Post, Perros
from .models import Perfil

admin.site.register(Post)
admin.site.register(Perros)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')