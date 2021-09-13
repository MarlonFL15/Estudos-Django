from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    nome_empresa = 'Nome da Empresa'
    descricao_empresa = 'Descrição da empresa'

    avaliacoes = [
        {"nome": "Avaliador 1", "local": "Brasil", "descricao": "Teste de avaliação 1"},
        {"nome": "Avaliador 2", "local": "Argentina", "descricao": "Teste avaliação 2"},
    ]
    #avaliacoes = []
    return render(request, 'index.html', {
        'nome_empresa':nome_empresa,
        'descricao_empresa': descricao_empresa,
        'avaliacoes': avaliacoes
    })

def about(request):
    return HttpResponse("About")

def contact(request, id):
    return HttpResponse("Contact: " + id)
