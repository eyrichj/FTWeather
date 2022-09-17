# Fuck the weather is a python program that
# scrapes data from the openweathermap api using your current latitude and longitude
# via geocoder and presents the weather in a cold and salty manor.
# Developed by Joe Gossett

# Imports
import requests, json
import geocoder

# geocoder
g = geocoder.ip('me')
lat = g.lat
lon = g.lng

#debug
print(lat, lon)

API_KEY = 'b2223f1470ff11a36f948d1bc8e037d1'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={API_KEY}'

winfo = requests.get(url).json()

winfo_id = (winfo['weather'][0]['id'])

if winfo_id >= (800):
    import l8xx.py







