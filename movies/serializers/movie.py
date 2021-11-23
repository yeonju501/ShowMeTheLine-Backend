from rest_framework import fields, serializers
from ..models import Genre, Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'line')

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    # 이 이름이 무조건 DB column이름과 같아야 함
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        # fields = ('id', 'duration', 'release_date', 'popularity', 'vote_average', 'poster_path', 'backdrop_path', 'director', 'actor', 'overview', 'line', 'genres')
        fields = '__all__'