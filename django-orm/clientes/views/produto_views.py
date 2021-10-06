from django.shortcuts import render

from ..forms import produto_form
def inserir_produto(request):
    form_produto = produto_form.ProdutoForm()

    return render('produtos/form_produto', {'form_produto': form_produto})