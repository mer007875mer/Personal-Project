# Generated by Django 4.2.5 on 2023-09-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_item_cast_remove_item_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cast',
            field=models.ManyToManyField(to='core.castcrew'),
        ),
        migrations.AddField(
            model_name='item',
            name='genre',
            field=models.ManyToManyField(to='core.genre'),
        ),
        migrations.AddField(
            model_name='item',
            name='production_countries',
            field=models.ManyToManyField(to='core.productioncountries'),
        ),
    ]