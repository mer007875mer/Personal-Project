from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.URLField(default='#')
    price = models.CharField(max_length=100)
    buy_url = models.URLField()
    date = models.DateTimeField(default=datetime.now)
    date_day = models.CharField(max_length=3, default='D')
    date_month = models.CharField(max_length=3, default='M')
    date_year = models.CharField(max_length=5, default='YYYY')
    image_src = models.URLField(default=None)

    def __str__(self):
        return self.title