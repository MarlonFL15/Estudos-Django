from ..models import Pedido

def cadastrar_pedido(pedido):
    return Pedido.objects.create(cliente = pedido.cliente, valor = pedido.valor, status=pedido.status,
                                   data_pedido = pedido.data_pedido, observacoes=pedido.observacoes)
def listar_pedidos():
    return Pedido.objects.all()

def listar_pedido_id(id):
    return Pedido.objects.get(id=id)

def editar_pedido(pedido_antigo, pedido_novo):
    pedido_antigo.cliente = pedido_novo.cliente
    pedido_antigo.valor = pedido_novo.valor
    pedido_antigo.status = pedido_novo.status
    pedido_antigo.data_pedido = pedido_novo.data_pedido
    pedido_antigo.observacoes = pedido_novo.observacoes

    pedido_antigo.save(force_update=True)