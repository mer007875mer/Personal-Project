# Generated by Django 4.2.3 on 2023-07-09 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]