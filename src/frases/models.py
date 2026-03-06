from django.db import models
from autores.models import Autores

# Create your models here.

class Frases(models.Model):
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    frase = models.TextField()
    fecha_frase = models.DateField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.visible} - {self.autor} - "{self.frase[:50]}"'
    