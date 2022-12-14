from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from . import models
from .forms import ReviwForm

class mainPageView(ListView):
    model = models.Movie
    template_name = "main.html"
    # queryset = models.Movie(id=1)

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

class ReviewUpdateView(UpdateView):
    model = models.Reviews
    template_name = 'review_edit.html'
    fields = ['text']
    success_url = reverse_lazy('main')
class ReviewDeleteView(DeleteView):
    model = models.Reviews
    template_name = 'review_delete.html'
    success_url = reverse_lazy('main')