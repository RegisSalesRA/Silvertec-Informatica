# Generated by Django 3.1.6 on 2021-02-16 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acessorios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('marca', models.CharField(choices=[('INTEL', 'INTEL'), ('AMD', 'AMD'), ('INTEL E AMD', 'INTEL E AMD')], max_length=100)),
                ('descricao', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Processador',
                'verbose_name_plural': 'Processadores',
            },
        ),
        migrations.CreateModel(
            name='PlacaMae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('marca', models.CharField(choices=[('INTEL', 'INTEL'), ('AMD', 'AMD'), ('INTEL E AMD', 'INTEL E AMD')], max_length=100)),
                ('slots', models.IntegerField(default=0)),
                ('memoria_suportada', models.PositiveIntegerField(choices=[(8, 8), (16, 16), (32, 32), (64, 64)])),
                ('video_integrado', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acessorios.cores')),
            ],
            options={
                'verbose_name': 'Placa Mãe',
                'verbose_name_plural': 'Placas Mãe',
            },
        ),
        migrations.CreateModel(
            name='PlacaDeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acessorios.cores')),
            ],
            options={
                'verbose_name': 'Placa de video',
                'verbose_name_plural': 'Placas de video',
            },
        ),
        migrations.CreateModel(
            name='MemoriaRam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('memoria', models.PositiveIntegerField(choices=[(8, 8), (16, 16), (32, 32), (64, 64)])),
                ('descricao', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acessorios.cores')),
            ],
            options={
                'verbose_name': 'Memoria',
                'verbose_name_plural': 'Memorias',
            },
        ),
    ]
