from ..models import Endereco

def cadastrar_endereco(endereco):
    return Endereco.objects.create(rua = endereco.rua, bairro = endereco.bairro, numero = endereco.numero,
                            pais = endereco.pais, complemento = endereco.complemento, cidade = endereco.cidade)
                        
def listar_endereco_id(id):
    return Endereco.objects.get(id=id)

def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.numero = endereco_novo.numero
    endereco_antigo.bairro = endereco_novo.bairro
    endereco_antigo.pais = endereco_novo.pais
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.complemento = endereco_novo.complemento
    endereco_antigo.save(force_update = True)

def remover_endereco(endereco):
    endereco.delete()