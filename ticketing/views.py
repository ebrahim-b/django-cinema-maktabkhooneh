from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    response_text = '\n'.join(
        '{}: {}'.format(i, movie) for i,movie in enumerate(movies, start=1)
    )
    return HttpResponse(response_text)
