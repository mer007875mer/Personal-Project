import rest_framework_simplejwt.authentication
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializers
from django.shortcuts import get_object_or_404
from api.authentication import TokenAuthentication


class ProductDetailAPIView(generics.RetrieveAPIView):  # GET Methods
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    authentication_classes = [authentication.SessionAuthentication,
                              TokenAuthentication,  # this one is custom
                              # authentication.TokenAuthentication  # this one is built-in
                              rest_framework_simplejwt.authentication.JWTAuthentication
                              ]
    permission_classes = [permissions.DjangoModelPermissions]


class ProductListAPIView(generics.ListAPIView):  # GET Methods
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    authentication_classes = [authentication.SessionAuthentication,
                              TokenAuthentication,  # this one is custom
                              # authentication.TokenAuthentication  # this one is built-in
                              rest_framework_simplejwt.authentication.JWTAuthentication
                              ]
    permission_classes = [permissions.DjangoModelPermissions]


class ProductListCreateAPIView(generics.ListCreateAPIView):  # POST Methods
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    authentication_classes = [authentication.SessionAuthentication,
                              TokenAuthentication,  # this one is custom
                              # authentication.TokenAuthentication  # this one is built-in
                              rest_framework_simplejwt.authentication.JWTAuthentication
                              ]
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save()


# use the function based to handle both at the same time
@api_view
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is None:
            # Detail View
            obj = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializers(data=obj, many=False)
            return Response(serializer.data)
        else:
            obj = Product.objects.all()
            serializer = ProductSerializers(data=obj, many=True)
            return Response(serializer.data)

    if method == "Post":
        # create an object
        serializer = ProductSerializers(data=request.data)
        serializer.save()
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)


