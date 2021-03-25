from django.urls import path
from . import views

app_name = 'ticketing'

urlpatterns = [
    path('movie/list/', views.movie_list, name = 'movie_list'),
    path('movie/details/<int:movie_id>', views.movie_details, name = 'movie_details'),
    path('cinema/list/', views.cinema_list, name = 'cinema_list'),
]