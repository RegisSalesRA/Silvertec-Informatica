# Generated by Django 3.1.2 on 2021-01-26 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0003_auto_20210121_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='montagem',
            old_name='nome',
            new_name='nome_usuario',
        ),
    ]