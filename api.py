import requests
import json
import numpy as np
import pandas as pd
import math

URL = "http://transportapi.com/v3/uk/places.json?&type=train_station&app_id=d9d3eca0&app_key=cfd4e8f645741a3d30ac1c0d776458c6"

location = "euston"
location2 = "edinburgh"

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


def disttrain(locA, locB): #Working out the distance obn ground
    R = 6373.0

    req = requests.get(url=URL, params=PARAMS)
    req2 = requests.get(url=URL, params=PARAMS2)
    data = req.json
    data2 = req2.json


    lat1 = data['member'][0]['latitude']
    lon1 = data['member'][0]['longitude']
    lat2 = data2['member'][0]['latitude']
    lon2 = data2['member'][0]['longitude']

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancet = R * c

    return distancet

locA = input("Start position :")
locB = input("Destination :")
flightce = 406.4 * distair(locA, locB)

traince = 65.6 * disttrain(locA, locB)

busce = 166.4 * disttrain(locA, locB)

Tubece = 195 * disttrain(locA, locB)

Coachce = 43.2 * disttrain(locA, locB)

Carce = 198.4 * disttrain(locA, locB)
