# Introdução

Esse projeto foi desenvolvido no decorrer do curso de `Django - Tópicos de segurança`, da [TreinaWeb](https://www.treinaweb.com.br/).
O Objetivo desse curso era mostrar como implementar os recursos de autenticação, login social, autorização e como o Django lida com os principais ataques a aplicações web, além de como resolvê-los.

### Conhecimentos adquiridos

* Como utilizar o módulo de autenticação padrão do Django;
* Como personalizar o módulo de autenticação do Django para se adequar a qualquer projeto;
* Como implementar o Login Social e, assim, permitir que os usuários possam se autenticar diretamente através do Google em nossa aplicação;
* Implementar a autorização e, assim, permitir que os usuários só possam acessar determinados recursos;
* Utilizar o Nginx para servir aplicações em servidores Ubuntu;

# Instalação e configuração

### Dependências

* Python 3
* MySQL

Dentro do diretório do projeto, baixe todas as bibliotecas necessárias:

    $ pip install -r requirements.txt

Após baixar as dependências, vá a até o arquivo `settings.py` na pasta `blog_treinaweb`. Você precisa fazer toda a configuração do seu banco de dados nas seguintes linhas:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

Após isso, é só realizar as migrações e iniciar o servidor:

    $ python manage.py migrate

    $ python manage.py runserver
