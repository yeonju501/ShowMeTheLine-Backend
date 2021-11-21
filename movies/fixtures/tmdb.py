import requests

class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def get_request_url(self, method='/movie/popular', **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'
        
        return request_url
    
    def get_movie_duration(self, id):
        request_url = f'https://api.themoviedb.org/3/movie/{id}'
        request_url += f'?api_key={self.api_key}'+ '&region=KR&language=ko'
        data = requests.get(request_url).json()
        duration = int(data.get('runtime'))
        return duration
    
    def get_actors_director(self, id):
        request_url = f'https://api.themoviedb.org/3/movie/{id}/credits'
        request_url += f'?api_key={self.api_key}'+ '&region=KR&language=ko'
        data = requests.get(request_url).json()
        director = ''
        actors = []

        for p in data.get('cast'):
            if p.get('job') == 'Director' and not director:
                director = p.get('name')
            if p['known_for_department'] =='Acting' and len(actors) < 5:
                actors.append(p.get('name'))
            if len(actors) == 5 and director:
                actors_str = ', '.join(actors)
                return director, actors_str

        for p in data.get('crew'):
            if p.get('job') == 'Director' and not director:
                director = p.get('name')
            if p['known_for_department'] =='Acting' and len(actors) < 5:
                actors.append(p.get('name'))
            if len(actors) == 5 and director:
                actors_str = ', '.join(actors)
                return director, actors_str

        actors_str = ', '.join(actors)
        return director, actors
            
