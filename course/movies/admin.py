from django.contrib import admin
from .models import Format, Genre, Movie, MovieImages, Actor, Rating, RatingStar

admin.site.register(Format)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieImages)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)