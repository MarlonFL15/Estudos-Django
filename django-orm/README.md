# Introdução

Este projeto foi desenvolvido no decorrer dos cursos de Banco de dados com Django ORM (parte 1 e 2), da TreinaWEB.
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

# Primeiros passos

### Dependências

* Python 3 e Django instalados
* MySQL
* Redis (para utilização de cache)

Abra o diretório do projeto e aplique as migrações:

    $ python manage.py migrate
    
Execute o servidor de desenvolvimento:

    $ python manage.py runserver
