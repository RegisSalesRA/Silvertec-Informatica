# Generated by Django 3.1.6 on 2021-02-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coolers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(choices=[('Padrao', 'Padrao'), ('Azul', 'azul'), ('Branco', 'branco'), ('Preto', 'preto'), ('Vermelho', 'Vermelho'), ('Colorido', 'Colorido')], max_length=100)),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
            },
        ),
        migrations.CreateModel(
            name='Cores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(choices=[('Padrao', 'Padrao'), ('Azul', 'azul'), ('Branco', 'branco'), ('Preto', 'preto'), ('Vermelho', 'Vermelho')], max_length=100)),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
            },
        ),
    ]
