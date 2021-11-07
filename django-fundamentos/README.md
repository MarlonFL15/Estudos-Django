# Introdução

Esse projeto foi desenvolvido no decorrer do curso de `Django Fundamentos`, da [TreinaWeb](https://www.treinaweb.com.br/).
O Objetivo desse curso era ter o primeiro contato com o django, aprender como implementar uma aplicação com acesso ao banco de dados com validações tanto no Back-end quanto no Front-end.

### Conhecimentos adquiridos

* O que é o Django e como funciona sua arquitetura;
* Como instalar o Django utilizando o PIP em qualquer sistema operacional;
* Como funciona cada uma das camadas da arquitetura do Django;
* Como criar filtros para melhorar a listagem dos dados;
* Como trabalhar com bancos de dados em aplicações Django;
* Como traduzir a aplicação desenvolvida para o português do Brasil;
* Como o Django trata alguns dos principais problemas de segurança presentes em aplicações web.

# Instalação e configuração

### Dependências

* Python 3
* MySQL

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