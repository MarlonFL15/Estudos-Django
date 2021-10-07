class Pedido():
    def __init__(self, cliente, valor, data_pedido, observacoes, status, produtos):
        self._cliente = cliente
        self._valor = valor
        self._data_pedido = data_pedido
        self._observacoes = observacoes
        self._status = status
        self._produtos = produtos

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def observacoes(self):
        return self._observacoes

    @observacoes.setter
    def observacoes(self, observacoes):
        self._observacoes = observacoes

    @property
    def data_pedido(self):
        return self._data_pedido

    @data_pedido.setter
    def data_pedido(self, data_pedido):
        self._data_pedido = data_pedido

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, produtos):
        self._produtos = produtos