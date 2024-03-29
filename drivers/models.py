from django.db import models

# Create your models here.

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(default='noname')
    start = models.TextField()
    end = models.TextField()
    stops = models.TextField()
    stops_arr = models.TextField(default='')
    date = models.DateField()
    time_dep = models.FloatField()
    time_arr = models.FloatField()
    car_model = models.TextField()
    car_cap = models.IntegerField()
    cigs = models.BooleanField()
    pets = models.BooleanField()
    price = models.FloatField()

    def __str__(self):
        return str(self.username)

class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(default='noname')
    start = models.TextField()
    end = models.TextField()
    distance = models.FloatField()
    date = models.DateField()
    time_dep = models.FloatField()
    time_arr = models.FloatField()
    cigs = models.BooleanField()
    pets = models.BooleanField()
    max_cost = models.FloatField()

    def __str__(self):
        return str(self.username)

class Ride(models.Model):
    ride_id = models.AutoField(primary_key=True)
    driver_ride_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passenger_ride_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver_username = models.TextField(default='noname')
    passenger_username = models.TextField(default='noname')
    date = models.DateField()
    pick_up = models.TextField()
    drop_off = models.TextField()



