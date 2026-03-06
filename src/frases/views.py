from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Frases

# Create your views here.

class FraseListView(LoginRequiredMixin,ListView):
    queryset = Frases.objects.all()
    template_name = 'frases/listar_frases.html'
    context_object_name = 'lista_frases'


class FraseVisibleListView(ListView):
    queryset = Frases.objects.filter(visible=True)
    template_name = 'frases/listar_frases.html'
    context_object_name = 'lista_frases'


class FraseNoVisibleListView(ListView):
    queryset = Frases.objects.filter(visible=False)
    template_name = 'frases/listar_frases.html'
    context_object_name = 'lista_frases'


class FraseCreateView(CreateView):
    model = Frases
    fields = ['autor', 'frase', 'fecha_frase']
    success_url = reverse_lazy('frases:listar_frases')
    template_name = 'crear.html'


class FraseUpdateView(UpdateView):
    model = Frases
    fields = '__all__'
    success_url = reverse_lazy('frases:listar_frases')
    template_name = 'crear.html'


class FraseDeleteView(DeleteView):
    model = Frases
    template_name = 'frases/borrar.html'
    success_url = reverse_lazy('frases:listar_frases')

@login_required
def detalle_frase(request, pk):
    frase = get_object_or_404(Frases, pk=pk)
    return render(request, 
                  'frases/detalle_frase.html',
                  {'frase':frase})



def modificar_activo(request, pk):
    frase_a_modificar = get_object_or_404(Frases,pk=pk)
    frase_a_modificar.visible = not frase_a_modificar.visible
    frase_a_modificar.save()
    return HttpResponseRedirect(reverse('frases:listar_frases'))



def listar_json(request):
    frases = get_list_or_404(Frases)
    frases_json = serializers.serialize('json', frases)
    return JsonResponse(frases_json, safe=False)