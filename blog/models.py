from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Perro(models.Model):
        ESTADO = ((1,'Disponible'),(2,'Rescatado'),(3,'Adoptado'))
        nombre = models.CharField(max_length=50)
        raza = models.CharField(max_length=50)
        desc = models.TextField()
        estado = models.CharField(max_length=20, choices=ESTADO, default='Rescatado')

class Usuario(models.Model):
        nombre = models.CharField(max_length=50)
        mail = models.CharField(max_length=50)
        rut = models.TextField()
        fechanac = models.DateTimeField()