from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy

from .models import Funcionario

from .forms import FuncionarioModelForm


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


class FuncionarioCreateView(CreateView):
    model = Funcionario
    template_name = 'funcionarios/form.html'
    fields = '__all__'
    success_url = reverse_lazy('funcionario_list')


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    template_name = 'funcionarios/form.html'
    fields = '__all__'
    success_url = reverse_lazy('funcionario_list')
    

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    context_object_name = 'funcionario'
    template_name = 'funcionarios/delete.html'
    success_url = reverse_lazy('funcionario_list')
