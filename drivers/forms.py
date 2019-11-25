from django import forms

class DriverForm(forms.Form):
    start = forms.CharField(label='start', max_length=20)
    end = forms.CharField(label='end', max_length=20)
    stops = forms.CharField(label='stops', max_length=100)
    date = forms.DateField(label='date', input_formats=['%d-%m-%Y', '%d/%m/%Y'])
    time_dep = forms.TimeField(label='time_dep')
    car_model = forms.CharField(label='car_model', max_length=50)
    car_cap = forms.IntegerField(label='car_cap')
    cigs = forms.BooleanField(label='cigs', required=False)
    pets = forms.BooleanField(label='pets', required=False)
    price = forms.FloatField(label='price')

class PassengerForm(forms.Form):
    start = forms.CharField(label='start', max_length=20)
    end = forms.CharField(label='end', max_length=20)
    date = forms.DateField(label='date', input_formats=['%d-%m-%Y', '%d/%m/%Y'])
    time_dep = forms.TimeField(label='time_dep')
    cigs = forms.BooleanField(label='cigs', required=False)
    pets = forms.BooleanField(label='pets', required=False)
    max_cost = forms.FloatField(label='max_cost')