import os
from datetime import datetime

import requests

API_KEY_FLIGHT = os.environ.get("API_KEY_FLIGHT")
NOW = datetime.now()

headers = {
    'apikey': API_KEY_FLIGHT,
}


class FlightSearch:

    def __init__(self):
        self.fly_from = 'LON'
        self.fly_to = 'PAR'
        # EDITOR NOTE: ERROR might be in the end of months cause month "dateFrom" should change from tomorrow
        self.dateFrom = datetime(year=NOW.year, month=NOW.month, day=((NOW.day+1) % 31)).strftime('%d/%m/%Y')
        self.dateTo = datetime(year=(NOW.year + (NOW.month + 5) // 12),
                               month=((NOW.month + 5) % 12) + 1,
                               day=NOW.day).strftime('%d/%m/%Y')
        self.endpoint = 'https://tequila-api.kiwi.com/v2/search'

    def make_params_flights(self):
        return {
            'fly_from': self.fly_from,
            'fly_to': self.fly_to,
            'dateFrom': self.dateFrom,
            'dateTo': self.dateTo
        }

    def get_flight_data(self):
        response_flight = requests.get(url=self.endpoint, params=self.make_params_flights(), headers=headers)
        return response_flight.json()['data']