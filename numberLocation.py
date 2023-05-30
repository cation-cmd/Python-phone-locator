""" import phonenumbers
from test import number

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number """


#NEW

#numberLocation.py

import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder

Key = "4efb9d7518a44c73b6432e370f18fcfb"

ch_nmber = phonenumbers.parse(number,"CH")
yourLocation = (geocoder.description_for_number(ch_nmber,"en"))
print(yourLocation)

#get service provider

from phonenumbers import carrier
service_provider =phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)


query=str(yourLocation)
results=geocoder.geocode(query)
#print(results)


lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup=yourLocation).add_to((myMap))

#save map in html file

myMap.save("myLocation.html")