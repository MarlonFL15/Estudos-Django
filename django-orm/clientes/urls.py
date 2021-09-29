from django.urls import path

from .views import listar_clientes, inserir_cliente, listar_cliente_id, editar_cliente, remover_cliente

#objetos que contém a rota, o método view correspondente e o "apelido" da rota
urlpatterns = [
    path('/listar', listar_clientes, name='listar_clientes'),
    path('/inserir', inserir_cliente, name='inserir_clientes'),
    path('/listar/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('/editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('/remover/<int:id>', remover_cliente, name='remover_cliente')
]