from django.contrib import admin

from .models import Item, Genre


admin.site.register(Item)
admin.site.register(Genre)
# admin.site.register(ProductionCountries)
# admin.site.register(CastCrew)