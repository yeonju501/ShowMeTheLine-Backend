from rest_framework import serializers
from rest_framework.utils import field_mapping
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
