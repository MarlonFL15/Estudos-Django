# Introdução

Esse projeto foi desenvolvido no decorrer dos cursos de `Banco de dados com Django ORM (parte 1 e 2)`, da [TreinaWeb](https://www.treinaweb.com.br/).
O Objetivo desses cursos era aprender como trabalhar com diferentes tipos de relacionamento, e estudar mais detalhadamente sobre como funciona o Django ORM.

### Conhecimentos adquiridos

* O que é e como implementar um CRUD com relacionamento 1-1;
* O que é e como implementar um CRUD com relacionamento 1-N;
* O que é e como implementar um CRUD com relacionamento N-N;
* Como otimizar consultas entre relações com Django;
* Como desfazer migrações no Django;
* Como mapear BDs legados com o Django ORM de forma automática.
* Como manipular bases de dados e gerar dados fakes para testes;
* Como configurar e utilizar Cache em projetos Django;
* Personalizar artefatos do BD com Django;
* Trabalhar com diferentes tipos de bancos de dados;
* Utilizar vários bancos de dados ao mesmo tempo em projetos Django.

# Instalação e configuração

### Dependências

* Python 3
* MySQL
* Redis em execução

Dentro do diretório do projeto, baixe todas as bibliotecas necessárias:

    $ pip install -r requirements.txt

Após baixar as dependências, vá a até o arquivo `settings.py` na pasta `tw_clientes`. Você precisa fazer toda a configuração do seu banco de dados nas seguintes linhas:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tw_django_fundamentos',
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
