# Introdução

Esse projeto foi desenvolvido no decorrer do curso de `Django - Desenvolvimento de APIs REST`, da [TreinaWeb](https://www.treinaweb.com.br/).
O Objetivo desse curso era aprender como implementar APIs REST utilizando o Django REST Framework.

### Conhecimentos adquiridos

* Como utilizar as classes de serialização do Django REST Framework;
* Como inserir, listar, editar e remover registros em uma API;
* O que é e como implementar o HATEOAS em nossa API;
* Implementar autenticação utilizando Token Bearer para proteger as funcionalidades da nossa API.

# Instalação e configuração

### Dependências

* Python 3
* MySQL

Dentro do diretório do projeto, baixe todas as bibliotecas necessárias:

    $ pip install -r requirements.txt

Após baixar as dependências, vá a até o arquivo `settings.py` na pasta `django_api`. Você precisa fazer toda a configuração do seu banco de dados nas seguintes linhas:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_rest',
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
