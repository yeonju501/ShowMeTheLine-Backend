from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.models import Review


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'like_movies')


class ProfileSerializer(serializers.ModelSerializer):
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'

    class FollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    
    followings = FollowSerializer(many=True, read_only=True)
    followers = FollowSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'followings', 'followers', 'review_set')
