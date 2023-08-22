from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializers


@api_view(['POST', 'GET'])
def api_home(request, *args, **kwargs):
    serializers = ProductSerializers(data=request.data)
    if serializers.is_valid(raise_exception=True):
        # instance = serializers.save()
        data = serializers.data
        return Response(data)
