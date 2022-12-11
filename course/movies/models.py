from datetime import date
from django.core.validators import FileExtensionValidator
from django.db import models

class Format(models.Model):
    name = models.CharField("Формат", max_length=100)
    # url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"

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
    format = models.ForeignKey(Format, verbose_name="Формат", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"



class MovieImages(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="static/movie_images/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return {self.value}

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


# class Reviews(models.Model):********************************

