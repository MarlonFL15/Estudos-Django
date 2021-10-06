from django.urls import path

from .views.cliente_views import *
from .views.pedido_views import *
#objetos que contém a rota, o método view correspondente e o "apelido" da rota
urlpatterns = [
    path('/listar_clientes', listar_clientes, name='listar_clientes'),
    path('/inserir_cliente', inserir_cliente, name='inserir_clientes'),
    path('/listar_cliente/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('/editar_clientes/<int:id>', editar_cliente, name='editar_cliente'),
    path('/remover_clientes/<int:id>', remover_cliente, name='remover_cliente'),
    path('/inserir_pedido', inserir_pedido, name='inserir_pedido'),
    path('/listar_pedidos', listar_pedidos, name='listar_pedidos'),
    path('/listar_pedido/<int:id>', listar_pedido_id, name='listar_pedido_id'),
    path('/editar_pedidos/<int:id>', editar_pedido, name='editar_pedido'),
]