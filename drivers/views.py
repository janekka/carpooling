from django.shortcuts import render, redirect
from .forms import DriverForm, PassengerForm
from drivers.models import Driver, Passenger
from django.http import HttpResponse
from .google_maps import get_distance, get_arrivals
import time
from calendar import timegm

# Create your views here.
def add_driver_view(request):
    form = DriverForm(request.POST)
    if form.is_valid() and request.user.is_authenticated:

        time_string = str(form.cleaned_data['date']) + 'T' + str(form.cleaned_data['time_dep'])
        time_stripped = time.strptime(time_string, '%Y-%m-%dT%H:%M:%S')
        epoch_time_dep = timegm(time_stripped)
        args = [form.cleaned_data['start'],]
        for el in form.cleaned_data['stops'].split():
            args.append(el)
        args.append(form.cleaned_data['end'])
        arr_times = get_arrivals(args)
        

        driver = Driver()
        driver.username = request.user.username
        driver.start = form.cleaned_data['start']
        driver.end = form.cleaned_data['end']
        driver.stops = form.cleaned_data['stops']
        driver.stops_arr = 
        driver.date = form.cleaned_data['date']
        driver.time_dep = epoch_time_dep
        driver.time_arr = epoch_time_dep + sum(arr_times)
        driver.car_model = form.cleaned_data['car_model']
        driver.car_cap = form.cleaned_data['car_cap']
        driver.cigs = form.cleaned_data['cigs']
        driver.pets = form.cleaned_data['pets']
        driver.price = form.cleaned_data['price']
        driver.save()
        return redirect('/')
    else:
        form = DriverForm()
    return render(request, 'add_driver.html', {'form':form})

def add_passenger_view(request):
    form = PassengerForm(request.POST)
    if form.is_valid() and request.user.is_authenticated:

        distance = get_distance((form.cleaned_data['start'],form.cleaned_data['end']))
        time_string = str(form.cleaned_data['date']) + 'T' + str(form.cleaned_data['time_dep'])
        print(time_string)
        time_stripped = time.strptime(time_string, '%Y-%m-%dT%H:%M:%S')
        epoch_time_dep = timegm(time_stripped)
        print(epoch_time_dep)

        passenger = Passenger()
        passenger.username = request.user.username
        passenger.start = form.cleaned_data['start']
        passenger.end = form.cleaned_data['end']
        passenger.distance = distance[0]/1000
        passenger.date = form.cleaned_data['date']
        passenger.time_dep = epoch_time_dep
        passenger.time_arr = epoch_time_dep+distance[1]
        passenger.cigs = form.cleaned_data['cigs']
        passenger.pets = form.cleaned_data['pets']
        passenger.max_cost = form.cleaned_data['max_cost']
        passenger.save()
        return redirect('/')
    elif request.user.is_authenticated:
        form = PassengerForm()
    else:
        return redirect('/')
    return render(request, 'add_passenger.html', {'form':form})
