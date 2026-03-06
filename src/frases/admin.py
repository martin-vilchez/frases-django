from django.contrib import admin
from .models import Frases
# Register your models here.

@admin.register(Frases)
class FrasesAdmin(admin.ModelAdmin):
    list_display = ('autor', 'visible', 'fecha_frase', 'creado_en')
    list_filter = ('visible', 'autor')
    search_fields = ('frase',)