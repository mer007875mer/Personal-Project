from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Main.urls")),
    path('register/', user_view.user_register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
