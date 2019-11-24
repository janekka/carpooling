import json
import numpy as np 
from datetime import datetime, date

def gen(n):
    data = []
    cities = ['Wroclaw', 'Warszawa', 'Krakow', 'Lodz', 'Poznan', 'Szczecin']
    for i in range(n):
        x = np.random.randint(6, size=2)
        if x[0]==x[1]:
            if x[1]==5:
                x[1] = x[1] - 1
            else:
                x[1] = x[1] + 1
    
        start = cities[x[0]]
        end = cities[x[1]]
        distance = float(len(end)*10)

        dic = {
            'model': 'drivers.Passenger',
            'pk' : i+1,
            'fields': {
                'user_id' : i,
                'start' : start, 
                'end' : end,
                'distance' : distance,
                'date' : str(date.today()),
                'time_dep' : str(datetime.now()),
                'time_arr' : str(datetime.now()),
                'cigs' : False,
                'pets' : False,
                'max_cost' : distance*((0.6-0.3)*np.random.rand()+0.3)
                }
            }
        data.append(dic)
    return data



with open('passengers.json', 'w') as outfile:
    json.dump(gen(40), outfile)