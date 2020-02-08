import requests
import jason
import django

def Flight(d):
    ce = 406.4 * d
    return ce


def distance(locA[], locB[]):
    R = 6373.0 #radius of earth


    lat1 = math.radians(52.2296756)  ## need to figure out how to get coordinates
    lon1 = math.radians(21.0122287)
    lat2 = math.radians(52.406374)
    lon2 = math.radians(16.9251681)

    dlon = lon2 - lon1
    change in coordinates

    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance
