from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    # response_text = '\n'.join(
    #     '{}: {}'.format(i, movie) for i,movie in enumerate(movies, start=1)
    # )

    response_text = """
        <html>
        <head>
        <title> لیست سینماها </title>
        </head>
        <body>
            <h1>فهرست سینماهای کشور</h1>
            <ul>
                {}
            </ul>
        </body>
        </html>
        """.format(
            '\n'.join('<li>{}</li>'.format(movie) for movie in movies)
        )
    return HttpResponse(response_text)