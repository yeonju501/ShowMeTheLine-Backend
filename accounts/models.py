from django.db import models
from django.contrib.auth.models import AbstractUser

from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    liked_movies = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
