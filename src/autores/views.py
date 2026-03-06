from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Autores

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def listar_autores(request):
    autores = Autores.objects.all()
    return render(request, 'autores/listar.html', {'autores':autores})


def detalle_autor(request, id):
    autor = get_object_or_404(Autores, id=id)
    return render(request, 'autores/detalle.html', {'autor':autor})


class AutoresDeleteView(DeleteView):
    model = Autores
    template_name= 'borrar.html'
    succes_url = reverse_lazy('autores:listar')


def modificar_activo(request, id):
    autor_a_modificar = get_object_or_404(Autores,id=id)
    autor_a_modificar.activo = not autor_a_modificar.activo
    autor_a_modificar.save()
    return HttpResponseRedirect(reverse('autores:listar'))


class AutoresVisiblesListView(ListView):
    queryset = Autores.objects.filter(activo=True)
    template_name = 'autores/listar.html'
    context_object_name = 'autores'


class AutoresNoVisiblesListView(ListView):
    queryset = Autores.objects.filter(activo=False)
    template_name = 'autores/listar.html'
    context_object_name = 'autores'


class AutoresCreateView(CreateView):
    model = Autores
    fields = '__all__'
    success_url = reverse_lazy('autores:listar')
    template_name = 'crear.html'


class AutoresUpdateView(UpdateView):
    model = Autores
    fields = '__all__'
    success_url = reverse_lazy('autores:listar')
    template_name = 'crear.html'



def listar_json(request):
    autores = get_list_or_404(Autores)
    autores_json = serializers.serialize('json', autores)
    return JsonResponse(autores_json, safe=False)