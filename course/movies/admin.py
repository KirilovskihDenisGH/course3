from django.contrib import admin
from .models import Genre, Movie, Actor, Reviews

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Reviews)