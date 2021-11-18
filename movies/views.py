from re import L
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers.movie import MovieSerializer, MovieListSerializer
from movies.models import Movie
from . import add_movie
# Create your views here.

@api_view(['GET', 'POST'])
def movie_list_or_create(request):
    def movie_list():
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def create_movie():
        movies = add_movie.add_movie()
        for movie in movies:
            serializer = MovieSerializer(data=movie)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return movie_list()
    elif request.method == 'POST':
        return create_movie()
