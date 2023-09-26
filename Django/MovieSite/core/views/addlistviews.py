from django.shortcuts import render, redirect
from django.views import View

from core.forms import AddItemForm
from core.models import Item, Genre
from core.utils import get_genre_names
from core.forms import SearchAddItemForm
from core.service import AddItemList, AddItem

messages = {
    600: "Connection failed. Please try again later.",
}


class AddMovieListView(View):
    template_name = 'add_movie_list.html'

    def get(self, request):
        form = SearchAddItemForm(request.GET)

        if not form.is_valid():
            page = request.GET.get('page', 1)

            search_series = AddItemList(page=page)
            search = search_series.get_movie_result_popular()
            if search == 600:
                return render(request, self.template_name, {"messages": messages[600]})

            search_result = search['results']

            genre = search_result[0]['genre_ids']
            genre = get_genre_names(genre)
            genre = {"genres": genre}

            context = {"result": search_result, **genre, **search}
            return render(request, self.template_name, context)

        page = request.GET.get('page', 1)
        name = form.cleaned_data.get('name')

        release_year = form.cleaned_data.get('release_year') or None

        search_series = AddItemList(
            page=page, query_name=name, release_year=release_year
        )
        search = search_series.get_movie_result()

        if search == 600:
            return render(request, self.template_name, {"messages": messages[600]})
 
        search_result = search['results']

        genre = search_result[0]['genre_ids']
        genre = get_genre_names(genre)
        genre = {"genres": genre}

        placeholder = {
            "name": request.GET.get('name', ''),
            "release_year": request.GET.get('release_year', '')
        }

        context = {"result": search_result, **genre, **search, **placeholder}
        return render(request, self.template_name, context)


class AddSeriesListView(View):
    template_name = 'add_series_list.html'

    def get(self, request):
        form = SearchAddItemForm(request.GET)

        if not form.is_valid():
            page = request.GET.get('page', 1)
            search_series = AddItemList(page=page)
            search = search_series.get_series_result_popular()

            if search == 600:
                return render(request, self.template_name, {"messages": messages[600]})

            search_result = search['results']

            genre = search_result[0]['genre_ids']
            genre = get_genre_names(genre)
            genre = {"genres": genre}

            context = {"result": search_result, **genre, **search}
            return render(request, self.template_name, context)

        page = request.GET.get('page', 1)
        name = form.cleaned_data.get('name')
        release_year = form.cleaned_data.get('release_year') or None

        search_series = AddItemList(
            page=page, query_name=name, release_year=release_year
        )
        search = search_series.get_series_result()  # Replace with get_series_result for series

        if search == 600:
            return render(request, self.template_name, {"messages": messages[600]})

        search_result = search['results']

        genre = search_result[0]['genre_ids']
        genre = get_genre_names(genre)
        genre = {"genres": genre}

        placeholder = {
            "name": request.GET.get('name', ''),
            "release_year": request.GET.get('release_year', '')
        }

        context = {"result": search_result, **genre, **search, **placeholder}
        return render(request, self.template_name, context)


class AddMovie(View):
    def post(self, request, movie_id):
        form = AddItemForm(request.POST)
        detail = AddItem(movie_id)
        detail_list = detail.get_movie_detail()

        if form.is_valid():
            movie_id = detail_list['id']


            try:
                item = Item.objects.get(movie_id=movie_id)
                messages.error(request, "Item with this ID already exists.")
                return redirect('search_movie_list')
            except Item.DoesNotExist:
                item = Item()

            item.overview = form.cleaned_data['overview']
            item.title = form.cleaned_data['title']

            item.movie_id = detail_list['id']
            item.adult = detail_list['adult']
            item.backdrop_path = detail_list['backdrop_path']
            item.imdb_id = detail_list['imdb_id']
            item.original_language = detail_list['original_language']
            item.original_title = detail_list['original_title']
            item.poster_path = detail_list['poster_path']
            item.lang = detail_list['original_language']
            item.release_date = detail_list['release_date']
            item.runtime = detail_list['runtime']
            item.status = detail_list['status']

            item.save()

            return redirect('search_movie_list')
        else:
            print(form.errors)
            return redirect('search_movie_list')

    def get(self, request, movie_id):

        form = AddItemForm()

        detail = AddItem(movie_id)
        detail_list = detail.get_movie_detail()
        credit_list = detail.get_movie_credit()

        if credit_list == 600 or detail_list == 600:
            return render(request, 'add_item.html', {"messages": messages[600]})

        context = {
            "title": detail_list['title'],
            "overview": detail_list['overview'],

            "adult": detail_list['adult'],
            "backdrop_path": detail_list['backdrop_path'],
            "imdb_id": detail_list['imdb_id'],
            "id": detail_list['id'],
            "original_language": detail_list['original_language'],
            "original_title": detail_list['original_title'],
            "poster_path": detail_list['poster_path'],
            "language": detail_list['original_language'],
            "release_date": detail_list['release_date'],
            "runtime": detail_list['runtime'],
            "status": detail_list['status'],
            "countries": detail_list['production_countries'],
            "genres": detail_list['genres'],
            "casts": credit_list['cast'][:15],
            "crew": credit_list['crew'],

            "form": form
        }

        return render(request, 'add_item.html', context)