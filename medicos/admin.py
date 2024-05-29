from django.contrib import admin

from medicos.models import Especialidades, Medico, Agenda

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    
class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'crm', 'telefono',
    ]
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'medico', 'horario'
    ]
    
admin.site.register(Especialidades, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Agenda, AgendaAdmin)