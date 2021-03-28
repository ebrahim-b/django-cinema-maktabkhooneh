from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def login_view(request):
    next_url = request.GET.get('next')
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
            #return HttpResponseRedirect(reverse('ticketing:showtime_list'))
            redirect_url = next_url if next_url else reverse('ticketing:showtime_list')
            return HttpResponseRedirect(redirect_url)
    else:
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        context= {}
    return render(request,'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile_details.html', context)

def profile_edit(request):
    pass
