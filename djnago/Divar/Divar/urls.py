from django.contrib import admin
from django.urls import path, include
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ScrapedApartmentsView.as_view(), name="scraped_apartments"),
]

