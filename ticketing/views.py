from django.shortcuts import render, get_object_or_404
from .models import Movie,Cinema


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie_list':movies
    }
    return render(request,'ticketing/movie_list.html',context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas':cinemas
    }
    return render(request,'ticketing/cinema_list.html',context)

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    context = {
        'movie': movie
    }
    return render(request,'ticketing/movie_details.html',context)