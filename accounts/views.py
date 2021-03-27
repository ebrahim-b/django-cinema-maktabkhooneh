from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is None:
            #return raise Http404("نام کاربری یا گذرواژه نادرست می باشد")
            context = {
                'username': username,
                'error' : 'کاربری با این مشخصات یافت نشد',
            }
        else:
            login(request, user)
            #return HttpResponse('خوش آمدید')
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        context= {}
    return render(request,'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
