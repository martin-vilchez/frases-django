from django.urls import path
from . import views
from .views import (
    FraseListView,
    FraseNoVisibleListView,
    FraseVisibleListView,
    FraseCreateView,
    FraseUpdateView,
    FraseDeleteView
)

app_name = 'frases'

urlpatterns = [
    path('listar/', FraseListView.as_view(), name = 'listar_frases'),
    path('crear/', FraseCreateView.as_view(), name = 'crear'),
    path('modificar/<int:pk>/', FraseUpdateView.as_view(), name='modificar'),
    path('borrar/<int:pk>/', FraseDeleteView.as_view(), name='borrar'),
    path('detalle_frase/<int:pk>/', views.detalle_frase, name='detalle_frase'),
    path('modificar_activo/<int:pk>/', views.modificar_activo, name='modificar_activo'),
    path("visibles/", FraseVisibleListView.as_view(), name="frases_visibles"),
    path('no_visibles/', FraseNoVisibleListView.as_view(), name='frases_no_visibles'),
    path('listar_json', views.listar_json, name='listar_json'),

]