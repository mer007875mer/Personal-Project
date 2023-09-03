from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=120, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def __str__(self):
        return self.title