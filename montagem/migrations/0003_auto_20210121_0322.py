# Generated by Django 3.1.3 on 2021-01-21 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0002_auto_20210121_0315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='montagem',
            old_name='placade_video',
            new_name='placa_de_video',
        ),
    ]
