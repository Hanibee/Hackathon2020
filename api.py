import requests
import json
import numpy as np
import pandas as pd

URL = "http://transportapi.com/v3/uk/places.json?&type=train_station&app_id=d9d3eca0&app_key=cfd4e8f645741a3d30ac1c0d776458c6"

location1 = "euston"
location2 = "edinburgh"

PARAMS = {'query':location}
PARAMS2 = {'query':location2}

def distair(locA, locB): #Working out the distance by air
    R = 6373.0

    df = pd.read_excel(r/Users/daishisuzuki/Desktop/airport.xlsx)
    print(df)

    lat1 = data['member'][0]['latitude']
    lon1 = data['member'][0]['longitude']
    lat2 = data2['member'][0]['latitude']
    lon2 = data2['member'][0]['longitude']

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancet = R * c


def disttrain(locA, locB): #Working out the distance obn ground
    R = 6373.0

    req = request.get(url=URL, params=PARAMS)
    req2 = request.get(url=URL, params=PARAMS2)
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

        flightce = 406.4 * distance

        traince = 65.6 * distancet

        busce = 166.4 * distancet

        Tubece = 195 * distancet

        Coachce = 43.2 * distancet

        Carce = 198.4 * distancet
