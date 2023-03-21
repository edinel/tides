#!/usr/bin/env python3

import pprint
import urllib
from urllib.request import urlopen
import json
from datetime import date, timedelta
pp=pprint.PrettyPrinter(indent=1)
station_id = "9414290" #Station ID for San Francisco; change to yours.


d=date.today() #get today's date
begin_date = d.strftime("%Y%m%d") #format today's date the way NOAA wants it
print (begin_date)
d = (date.today()+timedelta(days=7)) #7 days from now
end_date = d.strftime("%Y%m%d") #format the date 7 days hence the way NOAA wants it
print (end_date)


# There must be a beter way to do this# #this is fstrings innit#
url = ""
url+='https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date='
url+=begin_date
url+= '&end_date='
url+= end_date
url+= '&station='
url+= station_id
url+= '&product=predictions&datum=MLLW&time_zone=lst_ldt&interval=hilo&units=english&application=DataAPI_Sample&format=json'
#print (url)
response = urlopen(url)
data = json.loads(response.read())

pp.pprint(data)
print ("\n\n\n")
