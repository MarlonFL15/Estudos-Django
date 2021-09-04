class Cliente():
    def __init__(self, nome, sexo, data_nascimento, email, profissao):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.email = email
        self.profissao = profissao

        @property
        def nome(self):
            return self.nome

        @nome.setter
        def nome(self, nome):
            self.nome = nome

        @property
        def sexo(self):
            return self.sexo

        @sexo.setter
        def sexo(self, sexo):
            self.sexo = sexo

        @property
        def data_nascimento(self):
            return self.data_nascimento

        @data_nascimento.setter
        def data_nascimento(self, data_nascimento):
            self.data_nascimento = data_nascimento

        @property
        def email(self):
            return self.email

        @email.setter
        def email(self, email):
            self.email = email

        @property
        def profissao(self):
            return self.profissao

        @profissao.setter
        def profissao(self, profissao):
            self.profissao = profissao