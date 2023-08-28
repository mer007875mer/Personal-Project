from rest_framework_simplejwt import authentication as jwt
from drf_yasg.utils import swagger_auto_schema as swagger
from rest_framework import authentication as auth
from rest_framework import permissions as per
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from drf_yasg import openapi

from .models import Product
from . import serializers as sz


class ProductAPIView(APIView):

    authentication_classes = [auth.SessionAuthentication,
                              auth.TokenAuthentication,
                              jwt.JWTAuthentication
                              ]

    permission_classes = [per.IsAuthenticated]

    # Retrieve the Product list
    @swagger(
        query_serializer=sz.ProductListRequestSerializer,

        responses={
            status.HTTP_200_OK: sz.EntriesResponseSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_description="Get the list of products",
        operation_id="Product List",
        operation_summery="product list",
        tags=["product"]
    )
    def get(self, request):
        pg_serializer = sz.ProductListRequestSerializer(data=request.query_params)

        if pg_serializer.is_valid():
            page = pg_serializer.validated_data['page']
            count = pg_serializer.validated_data['count']
        else:
            return Response(pg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Product.objects.all()
        total_count = queryset.count()

        # Search
        search_query = request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        # Paginate
        paginator = Paginator(queryset, count)
        paginated_queryset = paginator.get_page(page)
        serializer = sz.ProductSerializer(paginated_queryset, many=True)

        response_data = {
            "returns": {
                "status": status.HTTP_200_OK,
                "message": "عملیات با موفقیت انجام شد."
            },
            "entries": {
                "list": serializer.data,
                "count": count,
                "page": page,
                "total_count": total_count
            }
        }
        return Response(response_data)

    # Create a Product
    @swagger(
        request_body=sz.ProductSerializer,
        responses={
            status.HTTP_201_CREATED: sz.ProductSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_description="Create a new product",
        operation_id="Create Product",
        operation_summery="create product",
        tags=["product"]
    )
    def post(self, request):
        serializer = sz.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
