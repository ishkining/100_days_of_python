import os

import requests

API_KEY = os.environ.get("API_WEATHER")

parameters = {
    'q': 'Birsk',
    'appid': API_KEY,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=parameters)
response.raise_for_status()

if int(response.json()['weather'][0]['id']) < 600:
    print('Bring an umbrella!')