# Generated by Django 4.2.4 on 2023-08-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, max_length=60, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]
