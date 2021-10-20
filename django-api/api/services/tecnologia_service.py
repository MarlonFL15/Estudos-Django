from ..models import Tecnologia

def listar_tecnologias():
    return Tecnologia.objects.all()