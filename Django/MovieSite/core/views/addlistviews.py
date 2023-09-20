from django.shortcuts import render, redirect
from core.service import AddItemList
from core.forms import AddItemForm
from django.views import View


class AddMovieListView(View):
    def get(self, request):
        form = AddItemForm(request.GET)


        # if form.is_valid():
        if True:
            # page = form.cleaned_data.get('page')
            page = 1
            # name = form.cleaned_data.get('name')
            name = "batman"
            # include_adult = form.cleaned_data.get('include_adult')
            include_adult = None
            # release_year = form.cleaned_data.get('release_year')
            release_year = 2022

            search_series = AddItemList(
                page=page, query_name=name, include_adult=include_adult, release_year=release_year
            )
            search_result = search_series.get_movie_result()
            print(search_result)
            return render(request, 'add_movie.html', {"result": search_result})
        else:
            # Handle the case where the form is not valid, e.g., return an error message or redirect
            return render(request, 'add_movie.html', {"error_message": "Invalid form data"})


class AddSeriesListView(View):
    def get(self, request):
        form = AddItemForm(request.GET)

        if form.is_valid():
            page = form.cleaned_data.get('page')
            name = form.cleaned_data.get('name')
            include_adult = form.cleaned_data.get('include_adult')
            release_year = form.cleaned_data.get('release_year')

            search_series = AddItemList(
                page=page, query_name=name, include_adult=include_adult, release_year=release_year
            )
            search_result = search_series.get_series_result()
            return render(request, 'add_series.html', {"result": search_result})
        else:
            # Handle the case where the form is not valid, e.g., return an error message or redirect
            return render(request, 'add_series.html', {"error_message": "Invalid form data"})
