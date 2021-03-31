from data_manager import DataManager, DATA
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()  # creates a Data Manager object


# sheet_data = data_manager.data_retrieve() #this retrieve the data of the Google Sheet via a GET request to  Sheety API

sheet_data = DATA  # set the variable to the hardcoded data
# pprint(sheet_data)

users_data = data_manager.get_customer_emails()  # gets the data about customers
search_engine = FlightSearch()  # creates a FlightSearch object

# for destination in sheet_data:
    #search_engine.add_city_names(destination) adds cities'names into the class

# cities = search_engine.add_city_code()  returns a list of dictionaries made up of the cities names and their IATA code

# data_manager.data_update_city_code(cities)  update our original data set with the IATA code

flight_data_engine = FlightData(sheet_data)  # creates a FlightData object

flight_prices = flight_data_engine.find_flight()  # returns a list of dictionaries with info about flights to each
# destination

notification_manager = NotificationManager(flights_data=flight_prices, flights_sheet=sheet_data, users_data=users_data)
notification_manager.compare_prices()  # checks if prices are lower than the threshold in our Google Sheet




