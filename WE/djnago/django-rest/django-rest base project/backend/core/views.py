from rest_framework.views import APIView

from .models import Product
from

class ProductListAPIView(APIView):
    def get(self, request):
        queryset = Product.object.al()
        serilaizer =
