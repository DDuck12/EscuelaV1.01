from django.db import models
from estudiantes.models import Estudiante

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=200)

    estudiantes = models.ManyToManyField(Estudiante, related_name='clases')

    def __str__(self):
        return self.nombre