from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.models import Movie

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class FollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    
    followings = FollowSerializer(many=True, read_only=True)
    followers = FollowSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'followings', 'followers')

class LikeSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    
    liked_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'like_movies')