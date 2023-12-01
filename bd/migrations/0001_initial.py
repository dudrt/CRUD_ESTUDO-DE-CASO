# Generated by Django 4.2.7 on 2023-11-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garçon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('cpf', models.BigIntegerField()),
                ('telefone', models.CharField(max_length=11)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=30)),
                ('rua', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('cpf', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=30)),
                ('rua', models.CharField(max_length=140)),
            ],
        ),
    ]