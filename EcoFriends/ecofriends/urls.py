"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path
from api import disttrain
from api import distbus
from api import disttube
train = []
bus = []
tube = []
location = "-0.133924,51.528135" #[array of long and lat] from the front end
location2 = "-0.088780,51.506383" #[array of long and lat] from the front end
distance = disttrain(location, location2)
distance_bus = distbus(location,location2)
distance_tube = disttube(location,location2)

for i in range(len(distance)):
    traince = 65.6 * distance[i]
    train.append(traince)
train.sort()
leastTrain = train[:1]
traindist = float(train[1])/65.6

for i in range(len(distance_bus)):
    busce = 166.4 * distance_bus[i]
    bus.append(busce)
bus.sort()
leastBus = bus[:1]
busdist = float(bus[1])/166.4

for i in range(len(distance_tube)):
    tubece = 195 * distance_tube[i]
    tube.append(tubece)
tube.sort()
leastTube = tube[:1]
tubedist = float(tube[1])/195

def index(request):
    return render(request, 'index.html',
    {
    "train_dist":traindist,
    "train_carbon":leastTrain,
    "bus_dist":busdist,
    "bus_carbon":leastBus,
    "tube_dist":tubedist,
    "tube_carbon":leastTube,

    })

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
]
