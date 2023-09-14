from django.contrib import admin
from django.urls import path, include
from Main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ScrapedApartmentsView.as_view(), name="scraped_apartments"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)