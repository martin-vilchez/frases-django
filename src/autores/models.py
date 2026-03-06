from django.db import models

# Create your models here.
class Autores(models.Model):
    NACIONALIDAD_CHOICES = [
        ('AR', 'Argentina'),
        ('FR', 'Francia'),
        ('ES','España'),
        ('OTRO', 'Otro')
    
    ]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacionalidades = models.CharField(
        max_length=35,
        choices=NACIONALIDAD_CHOICES,
        default='OTRO'
    )
    fecha_nacimiento=models.DateField(null=True, blank=True)
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
       
