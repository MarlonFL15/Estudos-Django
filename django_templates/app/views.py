from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    avaliacoes = [
        {"nome": "Avaliador 1", "local": "Brasil", "descricao": "Teste de avaliação 1"},
        {"nome": "Avaliador 2", "local": "Argentina", "descricao": "Teste avaliação 2"},
    ]
    #avaliacoes = []
    return render(request, 'index.html', {
        'avaliacoes': avaliacoes
    })

def about(request):
    return render(request, 'about.html')

def contact(request, id):
    return render(request, 'contact.html')
