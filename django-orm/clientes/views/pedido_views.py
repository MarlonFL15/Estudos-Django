from django.shortcuts import render, redirect

from ..forms import pedido_form
from ..entidades import pedido
from ..services import pedido_service

def inserir_pedido(request):
    if request.method == "POST":
        form_pedido = pedido_form.PedidoForm(request.POST)

        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data["cliente"]
            valor = form_pedido.cleaned_data["valor"]
            data_pedido = form_pedido.cleaned_data["data_pedido"]
            observacoes = form_pedido.cleaned_data["observacoes"]
            status = form_pedido.cleaned_data["status"]

            pedido_novo = pedido.Pedido(cliente=cliente, valor=valor, status=status, observacoes=observacoes,
                                        data_pedido=data_pedido)

            pedido_service.cadastrar_pedido(pedido_novo)
            return redirect('listar_pedidos')
    else:
        form_pedido = pedido_form.PedidoForm()
    return render(request, 'pedidos/form_pedido.html', {'form_pedido':form_pedido})

def listar_pedidos(request):
    pedidos = pedido_service.listar_pedidos()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

def listar_pedido_id(request, id):
    pedido = pedido_service.listar_pedido_id(id)
    return render(request, 'pedidos/lista_pedido.html', {'pedido': pedido})

def editar_pedido(request, id):
    pedido_antigo = pedido_service.listar_pedido_id(id)

    form_pedido = pedido_form.PedidoForm(request.POST or None, instance=pedido_antigo)

    if form_pedido.is_valid():
        cliente = form_pedido.cleaned_data["cliente"]
        valor = form_pedido.cleaned_data["valor"]
        data_pedido = form_pedido.cleaned_data["data_pedido"]
        observacoes = form_pedido.cleaned_data["observacoes"]
        status = form_pedido.cleaned_data["status"]

        pedido_novo = pedido.Pedido(cliente=cliente, valor=valor, status=status, observacoes=observacoes,
                                    data_pedido=data_pedido)

        pedido_service.editar_pedido(pedido_antigo, pedido_novo)
        return redirect('listar_pedidos')

    return render(request, 'pedidos/form_pedido.html', {'form_pedido':form_pedido})
