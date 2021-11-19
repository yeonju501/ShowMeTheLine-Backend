import requests
from .tmdb import TMDBHelper
from pprint import pprint

def add_movie():
    tmdb_helper = TMDBHelper('de3308aff80fcad45743238dc9bd4d0d')
    request_url = tmdb_helper.get_request_url(language = 'ko', region ='KR')
    movies_json = requests.get(request_url).json()
    movies = movies_json['results']
    for movie in movies:
        movie_id = movie['id']
        request_url = tmdb_helper.get_request_url(f'/movie/{movie_id}/keywords')
        keywords_json = requests.get(request_url).json()
        movie['keywords'] = keywords_json['keywords']
    return movies



