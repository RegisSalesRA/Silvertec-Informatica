# Generated by Django 3.1.2 on 2021-02-06 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_auto_20210206_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memoriaram',
            old_name='memoria_suportada',
            new_name='memoria',
        ),
    ]
