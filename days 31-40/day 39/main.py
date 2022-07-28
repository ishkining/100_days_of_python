# This file need to use the DataManager,FlightSearch, FlightData, NotificationManager to achieve the requirements.
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


data_manager = DataManager()

flight_data = FlightData()

notification_manager = NotificationManager()


for type_flight in data_manager.get_data():
    cheapest_way_data = flight_data.find_cheapest_way(type_flight['iataCode'], type_flight['lowestPrice'])
    if cheapest_way_data['had_function_found_way']:
        notification_manager.send_message(cheapest_way_data)


