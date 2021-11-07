# Introdução

Esse projeto foi desenvolvido no decorrer do curso de `Django - Módulo administrativo Django Admin`, da [TreinaWeb](https://www.treinaweb.com.br/).
O Objetivo desse curso era aprender como utilizar o Django Admin, módulo administrativo para gerenciamento de recursos de um projeto Django.

### Conhecimentos adquiridos

* Como ativar o Django Admin;
* Como registrar os models no Django Admin;
* Como utilizar Inline Forms no Django Admin;
* Personalizar o módulo administrativo com filtros e verbose names;
* Gerenciar o módulo de autenticação e autorização com o Django Admin.

# Instalação e configuração

### Dependências

* Python 3
* MySQL

Dentro do diretório do projeto, baixe todas as bibliotecas necessárias:

    $ pip install -r requirements.txt

Após baixar as dependências, vá a até o arquivo `settings.py` na pasta `django_admin`. Você precisa fazer toda a configuração do seu banco de dados nas seguintes linhas:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tw_django_admin',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Após isso, é só realizar as migrações e iniciar o servidor:

    $ python manage.py migrate

    $ python manage.py runserver
