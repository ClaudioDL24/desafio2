from django.contrib import admin
from .models import Tarea, Subtarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada')
    list_filter = ('eliminada',)
    search_fields = ('descripcion',)

@admin.register(Subtarea)
class SubtareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada', 'tarea')
    list_filter = ('eliminada',)
    search_fields = ('descripcion',)
    raw_id_fields = ('tarea',)