from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers.movie import MovieSerializer, MovieListSerializer
from movies.models import Movie
# Create your views here.

@api_view(['GET'])
def movie_list_or_create(request):
    # 목록 불러오기
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
