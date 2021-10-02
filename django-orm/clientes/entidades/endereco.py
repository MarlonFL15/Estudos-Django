class Endereco():
    def __init__(self, rua, bairro, numero, complemento, pais, cidade):
        self._rua = rua
        self._bairro = bairro
        self._numero = numero
        self._complemento = complemento
        self._pais = pais
        self._cidade = cidade

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, rua):
        self.rua = rua

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        self.bairro = bairro

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self.numero = numero

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        self.complemento = complemento

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self.cidade = cidade

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self.pais = pais