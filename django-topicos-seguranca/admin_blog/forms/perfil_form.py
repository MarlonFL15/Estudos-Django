from django import forms
from django.contrib.auth.forms import UserChangeForm
from ..models import Usuario

class FormPerfil(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'pais_origem']
