import os

import requests

API_KEY_SHEETY = os.environ.get("API_KEY_SHEETY")
NAME_OF_SHEET = os.environ.get("NAME_OF_SHEET")

headers_sheety = {
    'Authorization': os.environ.get("AUTHORIZATIONSHEET"),
}


class DataManager:

    def __init__(self):
        pass

    def get_data(self, column=''):
        get_endpoint = f'https://api.sheety.co/{API_KEY_SHEETY}/{NAME_OF_SHEET}/prices'
        response = requests.get(url=get_endpoint, headers=headers_sheety)
        if column == '':
            return response.json()['prices']
        else:
            try:
                return [city_data[column] for city_data in response.json()['prices']]
            except KeyError:
                return None
