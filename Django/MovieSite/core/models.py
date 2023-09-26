from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name


# class ProductionCountries(models.Model):
#     iso_3166_1 = models.CharField(max_length=2, unique=True, null=True)
#     name = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class CastCrew(models.Model):
#     cast_id = models.IntegerField(unique=True, null=True)
#     gender = models.IntegerField(null=True)
#     name = models.CharField(max_length=100, null=True)
#     job = models.CharField(max_length=100, null=True)
#     profile_path = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return f"{self.name}-{self.job}"


class Item(models.Model):
    title = models.CharField(max_length=100, null=True)
    overview = models.TextField(max_length=800, null=True)

    movie_id = models.IntegerField(unique=True, null=True)
    imdb_id = models.CharField(max_length=20, unique=True, null=True)
    original_title = models.CharField(max_length=100, null=True)
    release_date = models.CharField(max_length=15, null=True)
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=80, null=True)
    poster_path = models.CharField(max_length=80, null=True)
    language = models.CharField(max_length=10, null=True)
    runtime = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True)

    # production_countries = models.ManyToManyField(ProductionCountries)
    genre = models.ManyToManyField(Genre)
    # cast = models.ManyToManyField(CastCrew)

    def __str__(self):
        return self.original_title
