from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    release_date = models.DateField()
    genre = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    download = models.URLField()

    def __str__(self):
        return self.title