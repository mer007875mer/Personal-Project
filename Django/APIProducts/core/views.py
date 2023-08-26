from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(APIView):

    # Retrieve the Product list
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        response_data = {
            "returns": {
                "status": status.HTTP_200_OK,
                "message": "عملیات با موفقیت انجام شد."
            },
            "entries": {
                "list": serializer.data
            }
        }

        return Response(response_data)

    # Create a Product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            response_data = {
                "returns": {
                    "status": status.HTTP_201_CREATED,
                    "message": "محصول با موفقیت ایجاد شد."
                },
                "entries": {
                    "list": serializer.data
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "returns": {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "داده‌های ارسالی نامعتبرند."
                },
                "enteries": {
                    "list": serializer.errors
                }
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
