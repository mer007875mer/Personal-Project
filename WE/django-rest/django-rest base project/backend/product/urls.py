from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView
from api.views import SearchListView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="product-detail"),
    path('', ProductListCreateAPIView.as_view()),
    path('search/', SearchListView.as_view(), name='search')
]