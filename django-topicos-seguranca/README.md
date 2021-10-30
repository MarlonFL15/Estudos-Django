# Introdução

Este projeto foi desenvolvido no decorrer do curso de Django - Tópicos de segurança, da TreinaWEB.
O Objetivo desse curso era mostrar como implementar os recursos de autenticação, login social, autorização e como o Django lida com os principais ataques a aplicações web, além de como resolvê-los.

### Conhecimentos adquiridos

* Como utilizar o módulo de autenticação padrão do Django;
* Como personalizar o módulo de autenticação do Django para se adequar a qualquer projeto;
* Como implementar o Login Social e, assim, permitir que os usuários possam se autenticar diretamente através do Google em nossa aplicação;
* Implementar a autorização e, assim, permitir que os usuários só possam acessar determinados recursos;
* Utilizar o Nginx para servir aplicações em servidores Ubuntu.

# Primeiros passos

### Dependências

* Python 3 e Django instalados
* MySQL

Abra o diretório do projeto e aplique as migrações:

    $ python manage.py migrate
    
Execute o servidor de desenvolvimento:

    $ python manage.py runserver
