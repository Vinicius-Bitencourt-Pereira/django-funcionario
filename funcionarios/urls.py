from django.urls import path

from .views import(
    FuncionarioListView,
)


urlpatterns = [
    path('', FuncionarioListView.as_view(), name='funcionario_list'),
]
