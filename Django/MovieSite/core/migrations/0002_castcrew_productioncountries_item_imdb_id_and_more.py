# Generated by Django 4.2.5 on 2023-09-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_id', models.IntegerField(max_length=15, null=True, unique=True)),
                ('gender', models.IntegerField(max_length=15, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('job', models.CharField(max_length=25, null=True)),
                ('profile_path', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionCountries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_3166_1', models.CharField(max_length=2, null=True, unique=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='imdb_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='language',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='movie_id',
            field=models.IntegerField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='poster_path',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='release_date',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='runtime',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='adult',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='backdrop_path',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='original_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='overview',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='cast',
            field=models.ManyToManyField(to='core.castcrew'),
        ),
        migrations.AddField(
            model_name='item',
            name='production_countries',
            field=models.ManyToManyField(to='core.productioncountries'),
        ),
    ]
