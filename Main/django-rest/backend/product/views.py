from rest_framework.generics import RetrieveAPIView

from .models import Product
from .serializers import ProductSerializers


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # lookup_field = 'pk'