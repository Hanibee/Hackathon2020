import requests
import json
import numpy as np
import pandas as pd
import math

URL = "http://transportapi.com/v3/uk/places.json?&type=train_station&app_id=d9d3eca0&app_key=cfd4e8f645741a3d30ac1c0d776458c6"

location = "euston" #[array of long and lat] from the front end
location2 = "edinburgh" #[array of long and lat] from the front end

PARAMS = {'query':location}
PARAMS2 = {'query':location2}

def distair(locA, locB): #Working out the distance by air
    R = 6373.0

    df = pd.read_excel(r'/Users/daishisuzuki/Desktop/airport.xlsx')
    print(df)


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

req = requests.get (url=URL, params=PARAMS)
data = req.json



def disttrain(locA, locB):
    distance = []
    routeslen = len(data['routes'])
    partslen = len(data['route_parts'])
    coordlen = len(data['coordinates'])

    d = 0

    for i in routeslen:
        for j in partslen:
            for k in coorlen:
                if k == coorlen:
                    distance.append(d)
                else:
                    lat1 = data['routes'][i]['route_parts'][j]['coordinates'][k[1]]
                    lon1 = data['routes'][i]['route_parts'][j]['coordinates'][k[0]]
                    lat2 = data['routes'][i]['route_parts'][j]['coordinates'][k+1[1]]
                    lon2 = data['routes'][i]['route_parts'][j]['coordinates'][k+1[0]]

                    dlon = lon2 - lon1

                    dlat = lat2 - lat1

                    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

                    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                    dis = R * c
                    d = d + dis

    return

locA = input("Start position :")
locB = input("Destination :")
flightce = 406.4 * distair(locA, locB)

traince = 65.6 * disttrain(locA, locB)

busce = 166.4 * disttrain(locA, locB)

Tubece = 195 * disttrain(locA, locB)

Coachce = 43.2 * disttrain(locA, locB)

Carce = 198.4 * disttrain(locA, locB)
