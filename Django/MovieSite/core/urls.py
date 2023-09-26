from django.urls import path
from core.views.addlistviews import AddMovie, AddSeriesListView, AddMovieListView


urlpatterns = [
    path('add/movie/', AddMovieListView.as_view(), name="search_movie_list"),
    path('add/series/', AddSeriesListView.as_view(), name="search_series_list"),
    path('add/movie/<int:movie_id>/', AddMovie.as_view(), name="add_movie_list")
]