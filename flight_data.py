import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv(".env")

FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")
TEQUILA_SEARCH_URL = "https://tequila-api.kiwi.com/v2/search"


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, list_cities: list):
        self.price = 0
        self.departure_airport_code = "YMQ"
        self.departure_city = "Montreal"
        self.cities = list_cities
        self.api_key = FLIGHT_SEARCH_API_KEY
        self.search = TEQUILA_SEARCH_URL
        self.tomorrow = datetime.now() + timedelta(days=1)
        self.prices = []

    def find_flight(self):
        """find information about flights from Montreal to each destination in the data set"""
        current_date = self.tomorrow.strftime("%d/%m/%Y")

        six_months_from_tomorrow = self.tomorrow + timedelta(days=183)
        six_months_date = six_months_from_tomorrow.strftime("%d/%m/%Y")

        headers = {
            "apikey": self.api_key
        }

        for city in self.cities:
            parameters = {
                "fly_from": self.departure_airport_code,
                "fly_to": city['iataCode'],
                "date_from ": current_date,
                "date_to": six_months_date,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "max_stopovers": 3,
                "curr": "CAD"
            }

            response = requests.get(url=self.search, headers=headers, params=parameters)
            # print(response.raise_for_status())
            flight_response = response.json()
            flight_data = flight_response['data'][0]
            price = flight_data["price"]
            # print(flight_response['data'][0]['route'][0]['local_departure'])
            # print(flight_response['data'][0]['route'][-2]['local_departure'])
            # print(f"{city['city']}: ${price}")
            self.prices.append({
                "city_name": city['city'],
                "price": price,
                "arrival_code": city['iataCode'],
                "outbound": flight_response['data'][0]['route'][0]['local_departure'],
                "inbound": flight_response['data'][0]['route'][-2]['local_departure']
            })

        return self.prices
