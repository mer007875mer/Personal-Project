from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from api.validators import validate_title_no_admin, unique_product_title


class ProductSerializers(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user' ,read_only=True)
    url_2 = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validate_title_no_admin, unique_product_title])

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'url_2',
            'title',
            'content',
            'price',
            'sale_price'
        ]

    def validate_title(self, value):
        request = self.context.get("request")
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already exist")
        return value

    def get_url(self, obj):
        request = self.context.get("request")  # request.get
        if request is None:
            return None
        return reverse("product-detail", kwargs={'pk': obj.pk}, request=request)
