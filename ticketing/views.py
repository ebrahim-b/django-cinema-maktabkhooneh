from django.shortcuts import render, get_object_or_404
from .models import Movie,Cinema, ShowTime, Ticket
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
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

def cinema_details(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)

def showtime_list(request):
    # if request.user.is_authenticated and request.user.is_active:
    #     showtimes = ShowTime.objects.all().order_by('start_time')
    #     context = {
    #         'showtimes': showtimes
    #     }
    #     return render(request, 'ticketing/showtime_list.html', context)
    # else:
    #     return HttpResponse('ابتدا وارد شوید')

    showtimes = ShowTime.objects.all().order_by('start_time')
    context = {
        'showtimes': showtimes
    }
    return render(request, 'ticketing/showtime_list.html', context)

@login_required
def showtime_details(request, showtime_id):
    showtime = ShowTime.objects.get(pk=showtime_id)
    context = {
        'showtime': showtime
    }
    return render(request, 'ticketing/showtime_details.html', context)


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(customer=request.user.profile).order_by('-order_time')
    context = {
        'tickets': tickets
    }
    return render(request, 'ticketing/ticket_list.html', context)


@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'ticketing/ticket_details.html', context)