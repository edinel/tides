#!/usr/bin/env python3

import pprint
import urllib
from urllib.request import urlopen
import json
from geopy.distance import geodesic
from datetime import date, timedelta
noaa_token="WgHuVFVNsUIMTbWDUuSimEPjljQrveEU"
pp=pprint.PrettyPrinter(indent=2)
default_lat=37.73852307407762
default_lng=-122.42872556430657



def Get_Station_ID (lat=default_lat, lng=default_lng):
    all_tide_stations = json.load(urlopen("https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=tidepredictions&type=R")) 
    closest_station_id = ""
    closest_station=""
    distance = 100
    for station in (all_tide_stations["stations"]): 
        local_location = (lat, lng)
        station_location = station["lat"], station["lng"]
        calculated_distance = geodesic(local_location, station_location) 
        if calculated_distance < distance:
            if ((station ["reference_id"] != "") & (station ["type"] == "R")): 
                distance=calculated_distance
                closest_station_id = station["id"]
                closest_station=station
                print ("NEW CLOSEST STATION: ",closest_station_id,"\n\tname is",closest_station["name"],"\n\tdistance is", str(calculated_distance))
   
    return closest_station_id


station_id=str(Get_Station_ID()) #Get the closest station ID
d=date.today() #get today's date
begin_date = d.strftime("%Y%m%d") #format today's date the way NOAA wants it
d = (date.today()+timedelta(days=7)) #7 days from now
end_date = d.strftime("%Y%m%d") #format the date 7 days hence the way NOAA wants it



# There must be a beter way to do this# #this is fstrings innit#
url = ""
url+='https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date='
url+=begin_date
url+= '&end_date='
url+= end_date
url+= '&station='
url+= station_id
url+= '&product=predictions&datum=MLLW&time_zone=lst_ldt&interval=hilo&units=english&application=DataAPI_Sample&format=json'
response = urlopen(url)
tide_times_array = json.loads(response.read())["predictions"]
pp.pprint(tide_times_array)

