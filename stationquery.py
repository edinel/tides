#!/usr/bin/env python3

import pprint
import urllib
from urllib.request import urlopen
import urllib3
import json
from datetime import date, timedelta

noaa_token="WgHuVFVNsUIMTbWDUuSimEPjljQrveEU"
http = urllib3.PoolManager()
pp=pprint.PrettyPrinter(indent=1)
station_id = "9414290" #Station ID for San Francisco; change to yours.

my_lat = 37.73852307407762
my_long = -122.42872556430657
offset = .1

lat_lo = my_lat - offset
lat_hi = my_lat + offset
long_lo = my_long - offset
long_hi = my_long + offset


url = "https://www.ncei.noaa.gov/cdo-web/api/v2/stations?extent="
url += str(lat_lo)
url += ","
url += str(long_lo)
url += ","
url += str(lat_hi)
url += ","
url += str(long_hi)

print (url)

response = http.request(
    'GET',
    url,
    headers={
        'token': noaa_token
    }
)
data = json.loads(response.data.decode('utf-8'))
pp.pprint(data)
print ("\n\n\n")
