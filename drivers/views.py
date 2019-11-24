from django.shortcuts import render, redirect
from .forms import DriverForm
from drivers.models import Driver
from django.http import HttpResponse

# Create your views here.
def add_driver_view(request):
    form = DriverForm(request.POST)
    if form.is_valid() and request.user.is_authenticated:
        driver = Driver()
        driver.username = request.user.username
        driver.start = form.cleaned_data['start']
        driver.end = form.cleaned_data['end']
        driver.stops = form.cleaned_data['stops']
        driver.date = form.cleaned_data['date']
        driver.time_dep = form.cleaned_data['time_dep']
        driver.time_arr = form.cleaned_data['time_arr']
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
            