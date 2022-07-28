from datetime import datetime
import os

import requests

print(os.environ.get("APP_ID_NUTRITION"))
APP_ID_NUTRITION = os.environ.get("APP_ID_NUTRITION")
API_KEY_NUTRITION = os.environ.get("API_KEY_NUTRITION")
API_KEY_SHEETY = os.environ.get("API_KEY_SHEETY")
NAME_OF_SHEET = os.environ.get("NAME_OF_SHEET")


query_input = input('What have you done? ')

exercise_params = {
    'query': query_input,
    'gender': 'male',
    'weight_kg': 90,
    'height_cm': 167.64,
    'age': 22,
}

headers_nutrnutritionix = {
    'x-app-id': APP_ID_NUTRITION,
    'x-app-key': API_KEY_NUTRITION,
}

nutritionix_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response_exercise = requests.post(url=nutritionix_exercise_endpoint, json=exercise_params, headers=headers_nutrnutritionix)

print(response_exercise.json())

sheety_params = {
    'workout': {
        'date': datetime.now().strftime('%d/%m/%Y'),
        'time': datetime.now().strftime('%H:%M:%S'),
        'exercise': response_exercise.json()['exercises'][0]['name'],
        'duration': response_exercise.json()['exercises'][0]['duration_min'],
        'calories': response_exercise.json()['exercises'][0]['nf_calories'],
    }
}

headers_sheety = {
    'Authorization': 'Basic aXNoa2luaW5nOmlzaGtpbmluZzE5',
}

sheety_endpoint = f'https://api.sheety.co/{API_KEY_SHEETY}/{NAME_OF_SHEET}/workouts'

response_sheety = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers_sheety)

print(response_sheety.text)