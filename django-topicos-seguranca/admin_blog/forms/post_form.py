from django import forms
from upload_validator import FileTypeValidator

from ..models import Post, Categoria

class PostForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    capa = forms.FileField(validators=[FileTypeValidator(
        allowed_types=['images/jpeg']
    )])
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'conteudo', 'categoria', 'capa']