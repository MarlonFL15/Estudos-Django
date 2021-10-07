from django.shortcuts import redirect, render

from ..forms import produto_form
from ..entidades import produto
from ..services import produto_service

def listar_produtos(request):
    produtos = produto_service.listar_produtos()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def inserir_produto(request):
    if request.method == "POST":
        form_produto = produto_form.ProdutoForm(request.POST)

        if form_produto.is_valid():
            nome = form_produto.cleaned_data["nome"]
            valor = form_produto.cleaned_data["valor"]
            descricao = form_produto.cleaned_data["descricao"]

            produto_novo = produto.Produto(nome=nome, valor=valor, descricao=descricao)

            produto_service.cadastrar_produto(produto_novo)
            return redirect('listar_pedidos')
    else:
        form_produto = produto_form.ProdutoForm()
        return render(request, 'produtos/form_produto.html', {'form_produto': form_produto})