from django.contrib import admin
from .models import Autores

# Register your models here.

@admin.register(Autores)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidades', 'fecha_nacimiento', 'activo', 'creado_en')
    list_filter = ('nacionalidades', 'activo')
    search_fields = ('nombre',)