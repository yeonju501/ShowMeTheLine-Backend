from rest_framework import serializers
from ..models import Genre, Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'line')

class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        model = Genre
        fields = '__all__'
    
    # class KeywordSerializer(serializers.ModelSerializer):
    #     model = Keyword
    #     fields = '__all__'
    
    genres = GenreSerializer(many=True, read_only=True)
    # keywords = KeywordSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'duration', 'release_date', 'popularity', 'vote_average', 'poster_path', 'director', 'actor', 'overview', 'line', 'genres' )
    
