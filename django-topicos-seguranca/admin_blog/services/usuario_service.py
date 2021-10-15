from ..models import *

def cadastrar_usuario(usuario):
    usuario = Usuario.objects.create_user(nome = usuario.nome, email = usuario.email, pais_origem = usuario.pais_origem,
                                      password = usuario.password)

    usuario.save()