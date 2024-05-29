from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registro/', views.cliente_registro, name='cliente_registro'),
    path('actualizar/', views.cliente_actualizar, name='cliente_actualizar'),
    path('consultas/', views.consultar_lista, name='consulta_list'),
    path('consultas/crear/', views.consultar_registro, name='consulta_create'),
    path('consultas/editar/<int:pk>/', views.consultar_actualizar, name='consultas_update'),
    path('consultas/eliminar/<int:pk>/', views.consultar_eliminar, name='consultas_delete'),
]