import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")
# FLIGHT_SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/"
FLIGHT_SEARCH_API_LOCATIONS = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.cities = []
        self.api_key = FLIGHT_SEARCH_API_KEY
        self.location = FLIGHT_SEARCH_API_LOCATIONS

    def add_city_names(self, city):
        """Adds city to the list cities"""
        self.cities.append(city)  # takes a data set and assigns it to an attribute of the class

    def add_city_code(self):
        """Sets the IATA code for all cities"""

        for city in self.cities:
            headers = {
                "apikey": self.api_key
            }
            parameters = {
                "term": city['city'],
                "location_types": "city"
            }

            response = requests.get(url=self.location, headers=headers, params=parameters)
            data_response = response.json()

            print(response.raise_for_status())
            # print(data_response['locations'][0]['code'])

            city['iataCode'] = data_response['locations'][0]['code'] # sets the IATA code in our data set

        return self.cities  # returns data set

# city['iataCode'] = "Testing"
