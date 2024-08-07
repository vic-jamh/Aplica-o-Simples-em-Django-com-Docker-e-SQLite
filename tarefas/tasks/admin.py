from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')  # Campos a serem exibidos na lista
    list_filter = ('status',)  # Filtros disponíveis na lista
    search_fields = ('title', 'description')  # Campos pesquisáveis
