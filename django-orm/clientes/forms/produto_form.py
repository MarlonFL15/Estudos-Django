from django import forms

from ..models import Pedido, Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['valor', 'nome', 'descricao']
