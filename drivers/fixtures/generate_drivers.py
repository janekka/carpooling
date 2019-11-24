import json
import numpy as np 
from datetime import datetime, date

def gen(n):
    data = []
    cities = ['Wroclaw', 'Warszawa', 'Krakow', 'Lodz', 'Poznan', 'Szczecin']
    for i in range(n):
        ids = []
        for j in range(3):
            if j == 2:
                x = np.random.randint(6, size=3)
                for k in x:
                    if k in ids:
                        pass
                    else:
                        ids.append(k)
            else:
                y = np.random.randint(6)
                z = np.random.randint(6)
                if y == z and y == 5:
                    ids.append(y)
                    ids.append(z-1)
                elif y == z and not y == 5:
                    ids.append(y)
                    ids.append(z+1)
                else:
                    ids.append(y)
                    ids.append(z)
        start = cities[ids[0]]
        end = cities[ids[1]]
        stops = ''
        if len(ids) > 2:
            for g in range(2, len(ids), 1):
                stops = stops + cities[ids[g]] + ' '

        dic = {
            'model': 'drivers.Driver',
            'pk' : i+1,
            'fields': {
                'user_id' : n,
                'start' : start, 
                'end' : end,
                'stops' : stops,
                'date' : str(date.today()),
                'time_dep' : str(datetime.now()),
                'time_arr' : str(datetime.now()),
                'car_model' : 'Opel',
                'car_cap' : 4,
                'cigs' : False,
                'pets' : False,
                'price' : 0.43
                }
            }
        data.append(dic)
    return data



with open('drivers.json', 'w') as outfile:
    json.dump(gen(30), outfile)