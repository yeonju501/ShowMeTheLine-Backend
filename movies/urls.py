from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/review/', views.review_list_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_update_delete),
    path('bestFive/', views.bestFive),
]
