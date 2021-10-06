from django.db import models
from django.utils import timezone
# Create your models here.

class Endereco (models.Model):
    rua = models.CharField(max_length = 200, null = False, blank = False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def _str__(self):
        return self.rua

class Pedido (models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido Realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para Entrega")
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    data_pedido = models.DateField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(blank=False, max_length=1, null=False, choices=STATUS_CHOICES)
    observacoes = models.CharField(blank=True, max_length=50, null=True)
    

    def __str__(self):
        return self.cliente.nome

class Cliente (models.Model):

    choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length = 100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=choices)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
