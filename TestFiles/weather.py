import requests

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=0c4fdbac6d1f469b81c0b210034b5d4d&units=metric'.format(city)
#New API key on Openweathermaps under new email
res = requests.get(url)
data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']