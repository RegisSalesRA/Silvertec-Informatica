# Generated by Django 3.1.1 on 2020-11-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0015_auto_20201124_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='memoriaram',
            name='quantidade',
            field=models.CharField(blank=True, choices=[('2', '2'), ('4', '4')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='memoriaram',
            name='cor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]