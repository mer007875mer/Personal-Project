from django.urls import path
from core.views.addlistviews import AddSeriesListView, AddMovieListView


urlpatterns = [
    path('add/movie/', AddMovieListView.as_view(), name="search_movie_list"),
    path('add/series/', AddSeriesListView.as_view(), name="search_series_list")
]