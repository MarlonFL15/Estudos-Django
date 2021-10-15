from django.contrib.auth.base_user import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, pais_origem, password):
        if not email:
            raise ValueError('O usuário precisa de um email')
        usuario = self.model(
            nome = nome,
            email = self.normalize_email(email),
            pais_origem = pais_origem,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario