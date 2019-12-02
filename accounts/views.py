from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from drivers.models import Ride

# Create your views here.
def home_view(request, *args, **kwargs):
    info = {
        'user':request.user.is_authenticated,
        'username':request.user.username
    }
    return render(request, 'home.html', info)

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile_view(request):
    if request.user.is_authenticated:
        driver_rides = Ride.objects.filter(driver_username = request.user.username)
        passenger_rides = Ride.objects.filter(passenger_username = request.user.username)
        
        if len(driver_rides) == 0:
            driver_flag = False
        else:
            driver_flag = True

        if len(passenger_rides) == 0:
            passenger_flag = False
           
        else:
            passenger_flag = True
           
        
        #d_dates = driver_rides.date


        info = {
            'passenger_flag':passenger_flag,
            'driver_flag':driver_flag,
            'driver_rides':driver_rides,
            'passenger_rides':passenger_rides,
        }
        return render(request, 'profile.html', info)
    else:
        return redirect('home')