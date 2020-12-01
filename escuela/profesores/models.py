from django.db import models
from clases.models import Clase

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)

    clases = models.ManyToManyField(Clase, related_name='profesor')

    def __str__(self):
        return self.nombre