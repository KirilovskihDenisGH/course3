from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from . import models
from .forms import ReviwForm

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

class AddReview(View):
    def post(self, request, pk):
        form = ReviwForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie_id = pk
            form.save()
        return redirect("/")