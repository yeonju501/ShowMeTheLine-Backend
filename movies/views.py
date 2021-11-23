from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.review import ReviewSerializer
from .serializers.movie import MovieSerializer, MovieListSerializer
from movies.models import Genre, Movie, Review
from django.core import serializers
from django.core.paginator import Paginator
import random
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    # 목록 불러오기
    movies = Movie.objects.all().order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bestFive(request):
    movies = Movie.objects.all().order_by('-vote_average')[:20]
    # print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def review_list_create(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        movie = get_object_or_404(Movie, pk=movie_pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie, rank=0)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.review_set.filter(pk=review_pk).exist():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        serializer = ReviewSerializer(Review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response({'id': review_pk}, status=status.HTTP_204_NO_CONTENT)

# 메인 페이지 추천

@api_view(['GET'])
def line_recommend(request):
    genres = Genre.objects.all()
    movies = []
    for genre in genres:
        movie = genre.movie_set.all().order_by('?').first()
        movies.append(movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def line_recommend_result(request):
    # list
    movie_ids = request.data.ids
    genres_picked = []
    for id in movie_ids:
        movie = get_object_or_404(Movie, pk=id)
        gs = movie.genres.values('id')
        for g in gs:
            genres_picked.append(gs['id'])
    result_genres = random.randrange(genres_picked, 4)
    movies = []
    for g in result_genres:
        genre = Genre.objects.filter(id=g)
        movie = genre.movie_set.all().order_by('?').first()
        movies.append(movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    



    



