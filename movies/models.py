from django.db import models

# Create your models here.
# id는 자동으로 만들어짐

# class Keyword(models.Model):
#     name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(default=0)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    director = models.CharField(max_length=100, blank=True)
    actor = models.CharField(max_length=200, blank=True)
    overview = models.CharField(max_length=500)
    line = models.CharField(max_length=500, blank=True)
    genre = models.ManyToManyField(Genre)
    # keywords = models.ManyToManyField(Keyword)