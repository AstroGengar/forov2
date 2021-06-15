from django.db import models

# Create your models here.

class Genero(models.Model):
    #id --> numero autoincrementable
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class Anime(models.Model):
    nombre = models.CharField(max_length=200)
    capitulos = models.IntegerField(verbose_name="Capítulos")
    temporadas = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopsis = models.TextField(null=True, blank=True)
    fecha_emision = models.DateField()
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre