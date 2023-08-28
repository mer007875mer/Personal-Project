from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from core import views


schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v3.0',
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', views.ProductAPIView.as_view(), name='api'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/swagger/', schema_view.with_ui('swagger'))
]