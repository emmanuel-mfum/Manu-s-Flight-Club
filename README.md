# Manu-s-Flight-Club
Python app informing users via notifications about good flight deals on a set of destinations.

To make this program, we made full use of OOP in Python as well as APIs calls (namely to the Sheety, Twilio and Tequila APIs).

We have 2 Google Sheets, one with a list of destinations, their airport code and the lowest average price for a round trip to these places
according to Google Flights and another with a list of users of the flight club with their first name, last name and email.

The program will fetch data from both of these Google Sheets in time and make calls to the Tequila API for information about the flights going 
the destinations listed in the Google Sheet, then compared the prices found on the Tequila API to the one listed on the Google Sheet about destinations.

If a lower price than listed on the Google Sheet is found, the program will then use the Twilio API and the information about the customers on the second
Google Sheet to send emails and SMS on their mobile phones.

The program is split into five classes, each having its own role.

1.The Data Manager class is used for interacting with the Google Sheets via the Sheety API in order to retrieve the data found inside them
2.The Flight Data class is responsible for formatting the data in the form of a list of dictionaries and to make calls to the Tequila API in order to find infos about the flights.The data found is then used to populate that list of dictionaries  .
3.The Flight Search class was responsible for popuplating the Google sheet with destinations with the airport in the beginning.
4.The Notification Manager is tasked with comparing the prices listed on the Google sheet to those received from the Tequila API. If a lower price is found among the data sent by
the Tequila API, an SMS is sent as well as an email informing the member of my Flight Club to that a good flight deal is available and refering the member to a Google Flight link
about that particular destination.

To run to the program, simply run the "main.py" file.

The program will first retrieve the data from the list of destinations and their average flight prices from a Google Sheet via a method from the Data Manager class.
Then the data is sent to the Flight Data class, which uses it make dictionaries of a certain format and attach new flight prices, outbound and inbound dates to those destinations from the Tequila API.

The result is a list of dictionaries which sent to the Notification Manager class where thanks to the class method "compare_prices()", the prices from the Tequila API are 
compared to those from the Google Sheet. The method "compares_prices" takes a list of users (made with the Data Manager class), a list of flight infos (from the Flight Data  class) and a list of raw data from the destinations Google sheet.

Small notes

The data I am supposed to get from the Sheety API ( the destinations and their average flight prices) is hard coded in the Data Manager class as I didn't want to go over 
my limit of data requests for the Sheety API.

I realised that I don't have the phone numbers of my users in the second Google sheet with user informartion. This is a bit problematic for the call to the Twilio API
in the Notification Manager class (I tested my code using only my own phone number). To solve I would have to make a new column for the user's phone number in the Google sheet,
as well as modify a bit my code when taping into the user data in my Notification Manager class.

If a lower price is found in the flight informations gathered in the Flight Data class a SMS is sent to the user alerting him of a good deal. The "send_emails()" method is also
triggered, which using the user information from the Google sheet with user data (namely the email) will send the user an email also alerting him along with a Google Flights link.




