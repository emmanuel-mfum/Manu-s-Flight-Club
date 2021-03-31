import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")  # loads the environment file


sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

# In order to avoid going over my limit of requests at the Sheety API, once I updated correctly the iataCode using
# the Tequila API and got the final set of data for each city from the Sheety API I hardcoded the data set in the
# variable below. Therefore, when I run my program, I no longer use any method from this class.
DATA = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 800},
        {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 1300},
        {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 1100},
        {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 6000},
        {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 1400},
        {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 1400},
        {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 440},
        {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 500},
        {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 1100},
        {'city': 'Miami', 'iataCode': 'MIA', 'id': 11, 'lowestPrice': 400},
        {'city': 'Los Angeles', 'iataCode': 'LAX', 'id': 12, 'lowestPrice': 450},
        {'city': 'Cancun', 'iataCode': 'CUN', 'id': 13, 'lowestPrice': 500},
        {'city': 'Bogota', 'iataCode': 'BOG', 'id': 14, 'lowestPrice': 700},
        {'city': 'Rio de Janeiro', 'iataCode': 'RIO', 'id': 15, 'lowestPrice': 650},
        {'city': 'Santiago de Chile', 'iataCode': 'SCL', 'id': 16, 'lowestPrice': 670},
        {'city': 'London', 'iataCode': 'LON', 'id': 17, 'lowestPrice': 790},
        {'city': 'Amsterdam', 'iataCode': 'AMS', 'id': 18, 'lowestPrice': 1050},
        {'city': 'Madrid', 'iataCode': 'MAD', 'id': 19, 'lowestPrice': 700},
        {'city': 'Zürich', 'iataCode': 'ZRH', 'id': 20, 'lowestPrice': 700},
        {'city': 'Milan', 'iataCode': 'MIL', 'id': 21, 'lowestPrice': 1070},
        {'city': 'Prague ', 'iataCode': 'PRG', 'id': 22, 'lowestPrice': 1240},
        {'city': 'Munich', 'iataCode': 'MUC', 'id': 23, 'lowestPrice': 1320},
        {'city': 'Warsaw ', 'iataCode': 'WAW', 'id': 24, 'lowestPrice': 1440},
        {'city': 'Budapest', 'iataCode': 'BUD', 'id': 25, 'lowestPrice': 1355},
        {'city': 'Zagreb', 'iataCode': 'ZAG', 'id': 26, 'lowestPrice': 1340},
        {'city': 'Athens', 'iataCode': 'ATH', 'id': 27, 'lowestPrice': 890},
        {'city': 'Tallinn', 'iataCode': 'TLL', 'id': 28, 'lowestPrice': 1285},
        {'city': 'Saint Petersburg', 'iataCode': 'LED', 'id': 30, 'lowestPrice': 1215},
        {'city': 'Moscow', 'iataCode': 'MOW', 'id': 31, 'lowestPrice': 1220},
        {'city': 'Rabat', 'iataCode': 'RBA', 'id': 32, 'lowestPrice': 780},
        {'city': 'Brussels', 'iataCode': 'BRU', 'id': 35, 'lowestPrice': 962},
        {'city': 'Seoul', 'iataCode': 'SEL', 'id': 38, 'lowestPrice': 1385},
        {'city': 'Taipei', 'iataCode': 'TPE', 'id': 39, 'lowestPrice': 1030},
        {'city': 'Manilla', 'iataCode': 'MNL', 'id': 40, 'lowestPrice': 1955},
        {'city': 'Singapore', 'iataCode': 'SIN', 'id': 41, 'lowestPrice': 1355},
        {'city': 'Hong Kong', 'iataCode': 'HKG', 'id': 42, 'lowestPrice': 1370},
        {'city': 'Jakarta', 'iataCode': 'JKT', 'id': 43, 'lowestPrice': 1105},
        {'city': 'Bangkok', 'iataCode': 'BKK', 'id': 44, 'lowestPrice': 1310},
        {'city': 'Vancouver', 'iataCode': 'YVR', 'id': 45, 'lowestPrice': 835},
        {'city': 'Mumbai', 'iataCode': 'BOM', 'id': 46, 'lowestPrice': 1050},
        {'city': 'Auckland', 'iataCode': 'AKL', 'id': 47, 'lowestPrice': 3000},
        {'city': 'Melbourne', 'iataCode': 'MEL', 'id': 48, 'lowestPrice': 6000},
        {'city': 'Brisbane ', 'iataCode': 'BNE', 'id': 49, 'lowestPrice': 6000}]


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        # self.data = []
        self.data = DATA
        self.customer_data = []

    def data_retrieve(self):
        """ Retrieves the data from a Google Sheet via a GET request to the Sheety API"""
        response = requests.get(url=sheety_endpoint)
        print(response.raise_for_status())
        data_response = response.json()
        self.data = data_response['prices']
        return self.data

    def data_update_city_code(self, list_cities):
        """ takes in a list of cities and updates the IATA code """
        self.data = list_cities

        for city in list_cities:  # this corresponds to the format of a row in the Google Sheet file
            sheety_row = {
                "price": {
                    "city": city['city'],
                    "iataCode": city['iataCode'],
                    "lowestPrice": city['lowestPrice']
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=sheety_row)  # sends data to Google
            # Sheet
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
