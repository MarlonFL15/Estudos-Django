from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed
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

class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.nome

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
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome

def pre_save_produto_receiver(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        produtos = instance.produtos.all()
        total = 0

        for i in produtos:
            total += i.valor
        instance.valor = total
        instance.save()

m2m_changed.connect(pre_save_produto_receiver, sender = Pedido.produtos.through)

class Cliente (models.Model):

    choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )


    class Meta:
        db_table = "cliente_sistema" #Para alterar o nome da tabela no banco de dados
        ordering = ['-data_nascimento'] #Para ordenar na hora de fazer a consulta

    nome = models.CharField(max_length = 100, null=False, blank=False)
    sobrenome = models.CharField(max_length=30, null=True)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=choices)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    #Especifica o nome da chave primária
    id_funcionario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100, null=False, blank=False)