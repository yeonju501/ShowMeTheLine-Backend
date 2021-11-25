from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from movies.serializers.movie import MovieListSerializer
from .serializers import ProfileSerializer, UserSerializer, SignupSerializer
from rest_framework.permissions import AllowAny
from .models import User
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error' : '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def like_movie_list(request):
    if request.method == 'GET':
        movies = request.user.like_movies.all().order_by('-popularity')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_info(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            #if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
            return Response({'id':user_pk}, status=status.HTTP_201_CREATED)

