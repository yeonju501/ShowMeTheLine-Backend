from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_or_create),
    
]
