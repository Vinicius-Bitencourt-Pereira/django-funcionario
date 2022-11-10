from django import forms

from .models import Funcionario


class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome', 
            'telefone', 
            'email', 
            'salario', 
            'data_contratacao', 
            'departamento'
        ]