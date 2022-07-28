from flight_search import FlightSearch


class FlightData:

    def __init__(self):
        self.flight_search = FlightSearch()
        self.cheapest_data = {
            'had_function_found_way': False,
        }

    def find_cheapest_way(self, fly_to, price):
        self.cheapest_data['price'] = price
        self.flight_search.fly_to = fly_to
        for flight in self.flight_search.get_flight_data():
            # EDITOR NOTE: You can also add if else equal and add all cheapest flights to have multiple choices
            if int(flight['price']) < self.cheapest_data['price']:
                self.cheapest_data['departure_aita'] = flight['flyFrom']
                self.cheapest_data['destination_aita'] = flight['flyTo']
                self.cheapest_data['departure_city'] = flight['cityFrom']
                self.cheapest_data['destination_city'] = flight['cityTo']
                self.cheapest_data['price'] = int(flight['price'])
                self.cheapest_data['departure_date'] = flight['utc_departure']
                self.cheapest_data['arrival_date'] = flight['utc_arrival']
                self.cheapest_data['had_function_found_way'] = True
        return self.cheapest_data


