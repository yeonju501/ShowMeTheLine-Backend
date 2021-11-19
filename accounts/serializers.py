from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

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