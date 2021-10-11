from mixer.backend.django import mixer

from clientes.models import Pedido

#Cria 100 registros fakes do pedido
mixer.cycle(100).blend(Pedido)
