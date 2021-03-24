from django.shortcuts import render
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie_list':movies
    }
    return render(request,'movie_list.html',context)