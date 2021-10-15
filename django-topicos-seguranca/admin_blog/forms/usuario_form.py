from django import forms
from ..models import Usuario

#Cria o model personalizado de usuário

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação de Senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'pais_origem']

    #Função para verificar se as senhas são iguais
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2  and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais')
        return password2

    #sobreescreevendo a função "save" para criptografar a senha
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user