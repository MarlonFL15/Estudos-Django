from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import ClienteForm, EnderecoForm
from .models import Cliente
from .entidades import cliente
from .services import cliente_service

# Create your views here.

# informações importantes.
# todo método recebe uma request e também retorna uma request
# Método de listar todos os clientes

def listar_clientes(request):
    clientes = cliente_service.lista_lientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes':clientes})

#@csrf_exempt (notação para remover o protocolo de segurança csrf)

#Método de inserir cliente
def inserir_cliente(request):

    #Verifica se a rota foi acionada com um método post (ou seja, se o formulário foi enviado)
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST) #recupera os dados enviados

        if form_cliente.is_valid(): #Com base na Classe ClienteForm, verifica se os campos enviados são válidos
            nome = form_cliente.cleaned_data["nome"]
            sexo = form_cliente.cleaned_data["sexo"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            profissao = form_cliente.cleaned_data["profissao"]
            email = form_cliente.cleaned_data["email"]

            cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento, profissao=profissao,
                                           email=email)
            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('listar_clientes')
        #caso o formulário seja inválido, o objeto form vai guardar os erros em uma variável, e quando o form for renderizado,
        #os erros vão ser buscados nessas variáveis e serão mostrados na tela
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente':form_cliente, 'form_endereco':form_endereco})

#Método de listar cliente por id
def listar_cliente_id(request, id):
    cliente = cliente_service.lista_lientes_id(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente':cliente})

#Método de editar cliente
def editar_cliente(request, id):
    cliente_antigo = cliente_service.lista_lientes_id(id)
    form = ClienteForm(request.POST or None, instance=cliente_antigo)

    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        data_nascimento = form.cleaned_data["data_nascimento"]
        profissao = form.cleaned_data["profissao"]
        email = form.cleaned_data["email"]

        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento, profissao=profissao,
                                       email=email)
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form':form})

def remover_cliente(request, id):
    cliente = cliente_service.lista_lientes_id(id)

    if request.method == "POST":
        cliente_service.remover_cliente(cliente)
        return redirect('listar_clientes')

    return render(request, 'clientes/confirma_exclusao.html', {'cliente':cliente})