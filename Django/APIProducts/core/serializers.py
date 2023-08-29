from rest_framework import serializers

from .models import Product


class ProductListRequestSerializer(serializers.Serializer):

    page = serializers.IntegerField(required=True)
    count = serializers.IntegerField(required=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price'
        ]


class EntriesResponseSerializer(serializers.Serializer):
    list = ProductSerializer(many=True)
    count = serializers.IntegerField()
    page = serializers.IntegerField()
    total_count = serializers.IntegerField()