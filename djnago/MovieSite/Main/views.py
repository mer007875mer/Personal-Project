from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie

# def home(request):
#     return render(request, 'Main/home.html', context={
#         'movies' : Movie.objects.all().order_by('title')
#     })

class HomePage(ListView):
    model = Movie
    template_name = "Main/home.html"
    context_object_name = "movies"
    ordering = ['title']
    paginate_by = 3

class MoviePage(DetailView):
    model = Movie

