# Generated by Django 3.1.3 on 2020-11-17 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_auto_20201117_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memoriaram',
            name='tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.tamanhos'),
        ),
    ]