from django.shortcuts import render

# Create your views here.
def index(request):
    nome_empresa = 'Nome da Empresa'
    descricao_empresa = 'Descrição da empresa'


    return render(request, 'index.html', {
        'nome_empresa':nome_empresa,
        'descricao_empresa': descricao_empresa
    })