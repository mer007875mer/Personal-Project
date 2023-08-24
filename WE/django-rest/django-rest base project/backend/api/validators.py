from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from product.models import Product

'''
def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError("admin username not allowed")
    return value
'''


def validate_title_no_admin(value):
    if "admin" in value.lower():
        raise serializers.ValidationError("admin username not allowed")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
