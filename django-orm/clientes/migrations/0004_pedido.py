# Generated by Django 3.2.6 on 2021-10-02 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField(default=django.utils.timezone.now)),
                ('valor', models.FloatField()),
                ('status', models.CharField(choices=[('P', 'Pedido Realizado'), ('F', 'Fazendo'), ('E', 'Saiu para Entrega')], max_length=1)),
                ('observacoes', models.CharField(blank=True, max_length=50, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
