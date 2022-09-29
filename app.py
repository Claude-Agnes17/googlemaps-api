import requests
import json

key = 'please api key'

address = input()

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + key)

data = r.text
jsonObject = json.loads(data)

addr = jsonObject['results'][0]['formatted_address']
lat = jsonObject['results'][0]['geometry']['location']['lat']
lng = jsonObject['results'][0]['geometry']['location']['lng']
print(addr)
print(lat)
print(lng)
