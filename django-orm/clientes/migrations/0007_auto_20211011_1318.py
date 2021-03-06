# Generated by Django 3.2.6 on 2021-10-11 17:18

from django.db import migrations

#migração para separar o nome e o sobrenome dos clientes

def separar_nome_sobrenome(apps, schema_editor):
    Cliente = apps.get_model('clientes', 'cliente') #Nome da app, nome do model

    for cliente in Cliente.objects.all():
        if " " in cliente.nome:
            nome, sobrenome = cliente.nome.split(" ", 1)
            cliente.nome = nome
            cliente.sobrenome = sobrenome
        else:
            cliente.sobrenome = ""

        cliente.save()

class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_cliente_sobrenome'),
    ]

    operations = [
        migrations.RunPython(separar_nome_sobrenome)
    ]
