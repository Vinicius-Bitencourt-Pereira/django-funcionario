from django.views.generic import (
    ListView,
    DetailView,
)

from .models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario
    context_object_name = 'funcionarios'
    template_name = 'funcionarios/index.html'
    paginate_by = 10
    ordering = ['nome']


class FuncionarioDetailView(DetailView):
    model = Funcionario
    context_object_name = 'funcionario'
    template_name = 'funcionarios/detalhes.html'