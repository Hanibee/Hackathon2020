import requests
import json
import numpy as np
# import pandas as pd
import math

URL_bus = "https://transportapi.com/v3/uk/public/journey/from/lonlat:-3.188228,55.952391/to/lonlat:0.013493,51.449753.json?app_id=14d93d84&app_key=51b1d5714b28ac94b105d6b9296c05b8&modes=bus&service=southeast"
URL_train ="https://transportapi.com/v3/uk/public/journey/from/lonlat:-3.188228,55.952391/to/lonlat:0.013493,51.449753.json?app_id=14d93d84&app_key=51b1d5714b28ac94b105d6b9296c05b8&modes=train&service=southeast"
URL_tube = "https://transportapi.com/v3/uk/public/journey/from/lonlat:-3.188228,55.952391/to/lonlat:0.013493,51.449753.json?app_id=14d93d84&app_key=51b1d5714b28ac94b105d6b9296c05b8&modes=tube&service=southeast"

"""
URL = "https://transportapi.com/v3/uk/public/journey/from/"
to = "/to/"

last = ".json?app_id=14d93d84&app_key=51b1d5714b28ac94b105d6b9296c05b8&modes=bus&service=tfl"

locA = input("Start position :")
locB = input("Destination :")
"""
location = "-3.188228,55.952391" #[array of long and lat] from the front end
location2 = "0.013493,51.449753" #[array of long and lat] from the front end

PARAMS = {}
PARAMS2 = {'query':location2}


#Urlfinal = URL + location + to + location2 + last
#print (Urlfinal)
"""
def distair(locA, locB): #Working out the distance by air
    R = 6373.0

    df = pd.read_excel(r'/Users/daishisuzuki/Desktop/airport.xlsx')
    #print(df)


    lat1 = df.loc[3,'latitude']
    lon1 = df.loc[3,'longitude']
    lat2 = df.loc[5,'latitude']
    lon2 = df.loc[5,'longitude']

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance
"""
req_train = requests.get(url=URL_train, params=PARAMS)
data_train = req_train.json()
req_bus = requests.get(url=URL_bus,params=PARAMS)
data_bus = req_train.json()
req_tube = requests.get(url=URL_tube,params=PARAMS)
data_tube = req_tube.json()
#dat = data['routes'][0]['route_parts'][0]['coordinates'][0]
#print ("%s"
#        %(dat))

def disttrain(locA, locB):
    R = 6373.0
    distance = []
    routeslen = len(data_train['routes'])

    d = 0.0

    for i in range(routeslen):
        for j in range(len(data_train['routes'][i]['route_parts'])-1):
            lenk = len(data_train['routes'][i]['route_parts'][j]['coordinates'])-1
            for k in range(len(data_train['routes'][i]['route_parts'][j]['coordinates'])):
                if k == lenk:
                    distance.append(d)
                else:
                    lat1 = float(data_train['routes'][i]['route_parts'][j]['coordinates'][k][1])
                    lon1 = float(data_train['routes'][i]['route_parts'][j]['coordinates'][k][0])
                    lat2 = float(data_train['routes'][i]['route_parts'][j]['coordinates'][k+1][1])
                    lon2 = float(data_train['routes'][i]['route_parts'][j]['coordinates'][k+1][0])

                    dlon = lon2 - lon1

                    dlat = lat2 - lat1

                    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

                    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                    dis = R * c
                    d = d + dis

    return distance

def distbus(locA, locB):
    R = 6373.0
    distance_bus = []
    routeslen = len(data_bus['routes'])

    d = 0.0

    for i in range(routeslen):
        for j in range(len(data_bus['routes'][i]['route_parts'])-1):
            lenk = len(data_bus['routes'][i]['route_parts'][j]['coordinates'])-1
            for k in range(len(data_bus['routes'][i]['route_parts'][j]['coordinates'])):
                if k == lenk:
                    distance_bus.append(d)
                else:
                    lat1 = float(data_bus['routes'][i]['route_parts'][j]['coordinates'][k][1])
                    lon1 = float(data_bus['routes'][i]['route_parts'][j]['coordinates'][k][0])
                    lat2 = float(data_bus['routes'][i]['route_parts'][j]['coordinates'][k+1][1])
                    lon2 = float(data_bus['routes'][i]['route_parts'][j]['coordinates'][k+1][0])

                    dlon = lon2 - lon1

                    dlat = lat2 - lat1

                    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

                    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                    dis = R * c
                    d = d + dis

    return distance_bus

def disttube(locA, locB):
    R = 6373.0
    distance_tube = []
    routeslen = len(data_tube['routes'])

    d = 0.0

    for i in range(routeslen):
        for j in range(len(data_tube['routes'][i]['route_parts'])-1):
            lenk = len(data_tube['routes'][i]['route_parts'][j]['coordinates'])-1
            for k in range(len(data_tube['routes'][i]['route_parts'][j]['coordinates'])):
                if k == lenk:
                    distance_tube.append(d)
                else:
                    lat1 = float(data_tube['routes'][i]['route_parts'][j]['coordinates'][k][1])
                    lon1 = float(data_tube['routes'][i]['route_parts'][j]['coordinates'][k][0])
                    lat2 = float(data_tube['routes'][i]['route_parts'][j]['coordinates'][k+1][1])
                    lon2 = float(data_tube['routes'][i]['route_parts'][j]['coordinates'][k+1][0])

                    dlon = lon2 - lon1

                    dlat = lat2 - lat1

                    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

                    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                    dis = R * c
                    d = d + dis

    return distance_tube

"""
flightce = 406.4 * distair(location, location2)
print ("Flight")
print (flightce)
"""
distance = disttrain(location, location2)
train = []
bus = []
tube = []
coach = []
tube = []

print ("Train")
for i in range(len(distance)):
    traince = 65.6 * distance[i]
    train.append(traince)
    print (traince)

train.sort()
print ("Train least")
print (train[:1])
distance_bus = distbus(location,location2)
print("Bus")
for i in range(len(distance_bus)):
    busce = 166.4 * distance_bus[i]
    bus.append(busce)
    print (busce)

bus.sort()
print("Bus least")
print(bus[:1])

print("Tube")
distance_tube = disttube(location,location2)
for i in range(len(distance_tube)):
    tubece = 195 * distance[i]
    tube.append(tubece)
    print (tubece)

tube.sort()
print("Tube least")
print(tube[:1])

print("Coach")
for i in range(len(distance)):
    coachce = 43.2 * distance[i]
    coach.append(coachce)
    print (coachce)

coach.sort()
print("Coach least")
print(coach[:1])
distance_tube = disttube(location,location2)
print("tube")
for i in range(len(distance_tube)):
    tubece = 195 * distance_tube[i]
    tube.append(tubece)

tube.sort()
print(tube[:1])
