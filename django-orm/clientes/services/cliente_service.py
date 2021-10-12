from ..models import Cliente, Endereco

def lista_lientes():
    #Lista todos os clientes do sexo feminino que nasceram depois de 01/01/1990
    #clientes = Cliente.objects.filter(sexo='F', data_nascimento__gt= '1990-01-01').all()

    #Lista todos os clientes, menos os que são do sexo feminino e que nasceram depois de 01/01/1990
    #clientes = Cliente.objects.exclude(sexo='F', data_nascimento__gt='1990-01-01')

    return Cliente.objects.all()

def lista_lientes_id(id):
    return Cliente.objects.get(id=id)

def remover_cliente(cliente):
    cliente.delete()

def cadastrar_cliente(cliente):
    return Cliente.objects.create(nome=cliente.nome, sexo=cliente.sexo, data_nascimento=cliente.data_nascimento,
                                  email=cliente.email, profissao=cliente.profissao, endereco = cliente.endereco,
                                  sobrenome=cliente.sobrenome)
def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.sexo = cliente_novo.sexo
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.email = cliente_novo.email
    cliente.profissao = cliente_novo.profissao
    cliente.endereco = cliente_novo.endereco
    cliente.sobrenome = cliente_novo.sobrenome
    cliente.save(force_update = True)


