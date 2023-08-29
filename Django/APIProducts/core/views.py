from rest_framework_simplejwt import authentication as jwt
from drf_yasg.utils import swagger_auto_schema as swagger
from rest_framework.throttling import UserRateThrottle
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import authentication as auth
from rest_framework import permissions as per
from django.core.paginator import Paginator
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework import status
from django.db.models import Q
import logging

from .models import Product
from . import serializers as sz
from . import custom_renderer as cs

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class ProductAPIView(APIView):

    authentication_classes = [auth.SessionAuthentication,
                              auth.TokenAuthentication,
                              jwt.JWTAuthentication
                              ]

    permission_classes = [per.IsAuthenticated]
    throttle_classes = [UserRateThrottle]

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
    @method_decorator(cache_page(60 * 15))
    def get(self, request):
        pg_serializer = sz.ProductListRequestSerializer(data=request.query_params)

        logger.info("hello from the log")

        if pg_serializer.is_valid():
            page = pg_serializer.validated_data['page']
            count = pg_serializer.validated_data['count']
        else:
            return cs.response_structure(status_code=status.HTTP_400_BAD_REQUEST, entries=pg_serializer.errors)

        queryset = cache.get('product_queryset')
        if queryset is None:

            logger.info("set the new qs in the cache")

            queryset = Product.objects.order_by('title')
            cache.set('product_queryset', queryset, 60 * 5)

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

        entries = {
            "list": serializer.data,
            "count": count,
            "page": page,
            "total_count": total_count
        }

        return cs.response_structure(status_code=status.HTTP_200_OK, entries=entries)

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
            "list": serializer.data,
            }
            cache.clear()
            return cs.response_structure(status_code=status.HTTP_201_CREATED, entries=response_data)
        else:
            response_data = {
                "list": serializer.errors,
            }
            return cs.response_structure(status_code=status.HTTP_400_BAD_REQUEST, entries=response_data)