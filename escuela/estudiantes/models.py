from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.CharField(max_length=20)
    grado = models.CharField(max_length=20)
    grupo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre