from django.http import Http404

from ..models import Vaga
from .tecnologia_service import listar_tecnologia_id
def cadastrar_vaga(vaga):
    vaga_bd = Vaga.objects.create(titulo = vaga.titulo, descricao = vaga.descricao, salario=vaga.salario,
                                  local = vaga.local, quantidade = vaga.quantidade, contato=vaga.contato,
                                  tipo_contratacao = vaga.tipo_contratacao)
    vaga_bd.save()
    for i in vaga.tecnologias:
        tecnologia = listar_tecnologia_id(i.id)
        vaga_bd.tecnologias.add(tecnologia)
    return vaga_bd

def editar_vaga(vaga_antiga, vaga_nova):
    vaga_antiga.titulo = vaga_nova.titulo
    vaga_antiga.descricao = vaga_nova.descricao
    vaga_antiga.salario = vaga_nova.salario
    vaga_antiga.local = vaga_nova.local
    vaga_antiga.quantidade = vaga_nova.quantidade
    vaga_antiga.contato = vaga_nova.contato
    vaga_antiga.tipo_contratacao = vaga_nova.tipo_contratacao
    vaga_antiga.tecnologias.set(vaga_nova.tecnologias)
    vaga_antiga.save(force_update = True)

def listar_vagas():
    return Vaga.objects.all()

def listar_vaga_id(id):
    try:
        return Vaga.objects.get(id=id)
    except:
        raise Http404

def remover_vaga(vaga):
    vaga.delete()
