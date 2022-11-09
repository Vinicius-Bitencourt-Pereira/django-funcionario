from django.urls import path

from .views import(
    FuncionarioListView,
    FuncionarioDetailView,
)


urlpatterns = [
    path('', FuncionarioListView.as_view(), name='funcionario_list'),
    path('funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),
]
