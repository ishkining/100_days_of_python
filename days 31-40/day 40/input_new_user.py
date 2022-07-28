import os

import requests

API_KEY_SHEETY = os.environ.get("API_KEY_SHEETY")
NAME_OF_SHEET = os.environ.get("NAME_OF_SHEET")

headers_sheety = {
    'Authorization': os.environ.get("AUTHORIZATIONSHEET"),
}

first_name = input('Enter first Name: ')
last_name = input('Enter last Name: ')
email = input('Enter your email: ')
re_entered_email = input('Reenter your email for validation: ')

if email == re_entered_email:
    params = {
        'user': {
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
        },
    }

    get_endpoint = f'https://api.sheety.co/{API_KEY_SHEETY}/{NAME_OF_SHEET}/users'
    response = requests.post(url=get_endpoint, json=params, headers=headers_sheety)
    print("You are in our club!")



