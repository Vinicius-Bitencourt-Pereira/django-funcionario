from django.urls import path

from .views import(
    FuncionarioListView,
    FuncionarioDetailView,
    FuncionarioCreateView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)


urlpatterns = [
    path('', FuncionarioListView.as_view(), name='funcionario_list'),
    path('funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),
    path('funcionario-cadastrar/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('funcionario-atualizar/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('funcionario-deletar/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionario_delete')
]
