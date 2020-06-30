from django.contrib import admin
from .models import Actividades, Normativa

# Register your models here.
class ActividadesAdmin(admin.ModelAdmin):
    readonly_fields = ['creado', 'actualizado']
    list_display = ['normativa', 'actividad', 'creado', 'actualizado']

class NormativaAdmin(admin.ModelAdmin):
    readonly_fields = ['creado', 'actualizado']
    list_display = ['provincia', 'norma', 'creado', 'actualizado']

admin.site.register(Actividades, ActividadesAdmin)
admin.site.register(Normativa, NormativaAdmin)