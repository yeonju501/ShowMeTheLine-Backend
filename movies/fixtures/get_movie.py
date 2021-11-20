# 영화정보를 API를 이용해서 가져오기

# 홈페이지  https://www.themoviedb.org/
# Document  https://developers.themoviedb.org/3
# https://api.themoviedb.org/3/movie/popular?api_key=de3308aff80fcad45743238dc9bd4d0d&language=ko&region=KR&page=1
# pip install requests
import json
import requests
from tmdb import TMDBHelper
# 1. movie 정보
result = []
tmdb_helper = TMDBHelper('de3308aff80fcad45743238dc9bd4d0d')
request_url = tmdb_helper.get_request_url(language = 'ko', region ='KR')
for page in range(1, 25):
    URL = request_url + f'&page={page}'
    raw_data = requests.get(URL).json()
    data = raw_data.get('results')
    for movie in data:
      if movie.get("original_language") == "ko" or movie.get("original_language") == "en": 
        movie_id = movie.get("id")
        duration = tmdb_helper.get_movie_duration(movie_id)
        director, actors = tmdb_helper.get_actors_director(movie_id)
        movie_dict = {
            "model" : "movies.movie",
            "pk" : movie_id,
            "fields" : {
                "title" : movie.get("title"),
                "duration" : duration,
                "release_date" : movie.get("release_date"),
                "popularity" : movie.get("popularity"),
                "vote_average" : movie.get("vote_average"),
                "poster_path" : movie.get("poster_path"),
                "backdrop_path" : movie.get("backdrop_path"),
                "actor" : actors,
                "director" : director,
                "overview" : movie.get("overview"),
                "line" : "",
                "genres" : movie.get("genre_ids"),
            }
        }
        result.append(movie_dict)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False, indent=4))

## 2. genre 정보

# data = [
#     {
#       "id": 28,
#       "name": "액션"
#     },
#     {
#       "id": 12,
#       "name": "모험"
#     },
#     {
#       "id": 16,
#       "name": "애니메이션"
#     },
#     {
#       "id": 35,
#       "name": "코미디"
#     },
#     {
#       "id": 80,
#       "name": "범죄"
#     },
#     {
#       "id": 99,
#       "name": "다큐멘터리"
#     },
#     {
#       "id": 18,
#       "name": "드라마"
#     },
#     {
#       "id": 10751,
#       "name": "가족"
#     },
#     {
#       "id": 14,
#       "name": "판타지"
#     },
#     {
#       "id": 36,
#       "name": "역사"
#     },
#     {
#       "id": 27,
#       "name": "공포"
#     },
#     {
#       "id": 10402,
#       "name": "음악"
#     },
#     {
#       "id": 9648,
#       "name": "미스터리"
#     },
#     {
#       "id": 10749,
#       "name": "로맨스"
#     },
#     {
#       "id": 878,
#       "name": "SF"
#     },
#     {
#       "id": 10770,
#       "name": "TV 영화"
#     },
#     {
#       "id": 53,
#       "name": "스릴러"
#     },
#     {
#       "id": 10752,
#       "name": "전쟁"
#     },
#     {
#       "id": 37,
#       "name": "서부"
#     }
#   ]

# result = []

# for genre in data:
#     genre_dict = {
#         "model" : "movies.genre",
#         "pk" : genre.get("id"),
#         "fields" : {
#             "name" : genre.get("name")
#         }
#     }
#     result.append(genre_dict)

# with open('genres.json', 'w', encoding='UTF-8') as file:
#     file.write(json.dumps(result, ensure_ascii=False, indent=4))