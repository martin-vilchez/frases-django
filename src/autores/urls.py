from django.urls import path
from . import views
from .views import (
    AutoresCreateView,
    AutoresNoVisiblesListView,
    AutoresDeleteView,
    AutoresUpdateView,
    AutoresVisiblesListView
)

app_name = 'autores'

urlpatterns = [
    path('home/', views.inicio, name='inicio'),
    path('listar/', views.listar_autores, name='listar'),
    path('detalle/<int:id>/', views.detalle_autor, name='detalle'),
    path('borrar/<int:pk>/', AutoresDeleteView.as_view(), name='borrar'),
    path('modificar_activo/<int:id>/', views.modificar_activo, name='modificar_activo'),
    path('visibles/', AutoresVisiblesListView.as_view(), name='autores_visibles'),
    path('no_visibles/', AutoresNoVisiblesListView.as_view(), name='autores_no_visibles'),
    path('crear/', AutoresCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>', AutoresUpdateView.as_view(), name='modificar'),
    path('listar_json', views.listar_json, name='listar_json')
]
