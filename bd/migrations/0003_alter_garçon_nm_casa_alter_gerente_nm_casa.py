# Generated by Django 4.2.7 on 2023-11-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0002_alter_garçon_options_alter_gerente_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garçon',
            name='nm_casa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gerente',
            name='nm_casa',
            field=models.IntegerField(),
        ),
    ]
