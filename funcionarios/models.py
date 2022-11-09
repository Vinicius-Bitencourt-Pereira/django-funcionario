from django.db import models


class Departamento(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=25,
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=True
    )

    salario = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        null=False,
        blank=False
    )

    data_contratacao = models.DateField(
        null=False,
        blank=False
    )

    departamento = models.ForeignKey(
        Departamento, 
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.nome
