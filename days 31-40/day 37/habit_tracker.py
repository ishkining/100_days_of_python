from datetime import datetime
import os

import requests

USERNAME = 'ishkining'
TOKEN = 'idontknowwhyilovetoeat'
GRAPH_ID = 'graphtest1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Test',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_data = {
    'date': datetime.now().strftime('%Y%m%d'),
    'quantity': '10',
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/' \
                  f'{datetime(year=2022, month=7, day=26).strftime("%Y%m%d")}'

new_pixel_data = {
    'quantity': '5'
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)