from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from . import models

from .models import Movie

# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})

class mainPageView(ListView):
    model = models.Movie
    template_name = "main.html"

class moviePageView(ListView):
    model = models.Movie
    template_name = "movies.html"

class cartoonsPageView(ListView):
    model = models.Movie
    template_name = "cartoons.html"

class serialsPageView(ListView):
    model = models.Movie
    template_name = "serials.html"

class animePageView(ListView):
    model = models.Movie
    template_name = "anime.html"

class movieDetailView(DetailView):
    model = models.Movie
    template_name = "detail.html"
