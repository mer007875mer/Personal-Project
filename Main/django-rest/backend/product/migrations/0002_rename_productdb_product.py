# Generated by Django 4.2.4 on 2023-08-22 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductDB',
            new_name='Product',
        ),
    ]
