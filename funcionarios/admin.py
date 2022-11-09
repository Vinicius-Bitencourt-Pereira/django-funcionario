from django.contrib import admin
from .models import Departamento, Funcionario


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome']
    list_per_page = 10
    search_fields = ['nome']


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'salario', 'data_contratacao', 'departamento']
    list_display_links = ['nome']
    ordering = ['nome']
    list_per_page = 10
    search_fields = ['nome', 'departamento']