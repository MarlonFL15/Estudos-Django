from django.http import Http404

from ..models import Tecnologia

def listar_tecnologias():
    return Tecnologia.objects.all()

def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome = tecnologia.nome)

def listar_tecnologia_id(id):
    try:
        return Tecnologia.objects.get(id = id)
    except:
        raise Http404

def editar_tecnologia(tecnologia_antiga, tecnologia_nova):
    tecnologia_antiga.nome = tecnologia_nova.nome
    tecnologia_antiga.save(force_update=True)

def remover_tecnologia(tecnologia):
    tecnologia.delete()