from datetime import date
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class Actor(models.Model):
    name = models.CharField("Имя", max_length=100)
    date_of_birth = models.DateField("Дата рождения", default=date.today)
    image = models.ImageField("Изображение", upload_to="static/actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры и режиссёры"
        verbose_name_plural = "Актёры и режиссёры"

class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    # url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="static/poster/")
    banner = models.ImageField("Банер", upload_to="static/banner/")
    video = models.FileField(upload_to="static/video/", default="cat.mp4")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2022)
    country = models.CharField("Страна", max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссёр", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актёры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    budget = models.PositiveSmallIntegerField("Бюджет", default=0, help_text="Сумма в долларах")
    fees_in_usa = models.PositiveSmallIntegerField("Сборы в США", default=0, help_text="Сумма в долларах")
    fees_in_world = models.PositiveSmallIntegerField("Сборы в мире", default=0, help_text="Сумма в долларах")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Комментарий", max_length=2000)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)
    # def __str__(self):
    #     return f"{self.name} - {self.movie}"

    def get_absolute_url(self):
        return reverse('detail')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

