from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('registro/medico/', views.medico_registro, name='medico_registro'),
    path('registro/especialidades/', views.especialidades_registro, name='especialidades_registro'),
    path('agenda/', views.agenda_registro, name='agenda_consulta'),
    path('agenda/actualizar/<int:pk>/', views.agenda_actualizar, name='agenda_consulta_actualizar'),
    path('agenda/apagar/<int:pk>/', views.agenda_borrar, name='agenda_consulta_borrar'),
    path('mi/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/medicos/', views.medico_lista, name="medicos_lista"),
    path('admim/lista/especialidades/', views.especialidades_lista, name="especialidades_lista")
    
]