from ..models import Cliente

def lista_lientes():
    return Cliente.objects.all()

def lista_lientes_id(id):
    return Cliente.objects.get(id=id)

def remover_cliente(cliente):
    cliente.delete()

def cadastrar_cliente(cliente):
    return Cliente.objects.create(nome=cliente.nome, sexo=cliente.sexo, data_nascimento=cliente.data_nascimento,
                                  email=cliente.email, profissao=cliente.profissao)
def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.sexo = cliente_novo.sexo
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.email = cliente_novo.email
    cliente.profissao = cliente_novo.profissao
    cliente.save(force_update = True)
