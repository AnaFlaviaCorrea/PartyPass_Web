# Generated by Django 4.2.1 on 2023-06-07 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0007_comandas_data_atual'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comandas',
            old_name='data_atual',
            new_name='ultima_recarga',
        ),
    ]
