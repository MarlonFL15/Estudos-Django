from ..models import Produto

def cadastrar_produto(produto):
    return Produto.objects.create(descricao = produto.descricao, valor = produto.valor, 
                                    nome = produto.nome)

def listar_produtos():
    return Produto.objects.all()

def listar_produto_id(id):
    return Produto.objects.get(id=id)