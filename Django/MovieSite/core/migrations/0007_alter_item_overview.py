# Generated by Django 4.2.5 on 2023-09-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_item_cast_remove_item_production_countries_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='overview',
            field=models.TextField(max_length=800, null=True),
        ),
    ]
