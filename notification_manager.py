import smtplib

from twilio.rest import Client  # Download helper library from Twilio

MY_EMAIL = "*******"
PASSWORD = "*****"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    # get 2 sets of data, one with the flight information, the other is from the Sheety API

    def __init__(self, flights_data, flights_sheet, users_data):
        self.price = 0
        self.departure_city_name = "Montreal"
        self.departure_airport_code = "YMQ"
        self.arrival_city = ""
        self.arrival_airport_code = ""
        self.outbound_date = ""
        self.inbound_date = ""
        self.flights_found = flights_data
        self.flights_thresholds = flights_sheet
        self.users = users_data
        self.account_sid = "ACcef81630918f6d71ee45fe0de66b85dd"  # account sid for twilio
        self.auth_token = "3983f8d3eefe913cbdd758ef2974866f"  # auth token for twilio

    def compare_prices(self):
        """For each city in the two data sets, checks if there is a lower price than can be found"""
        # If a lower price can be found in the data set we got from the Tequila API compared to the price listed
        # in the Google Sheet, then the program will send an SMS to the user alerting him about a good flight deal
        for city1, city2 in zip(self.flights_found, self.flights_thresholds):
            self.arrival_city = city2['city']
            self.arrival_airport_code = city2['iataCode']
            self.price = city2['lowestPrice']
            out = city1['outbound'].split("T")
            inb = city1['inbound'].split("T")
            self.outbound_date = out[0]
            self.inbound_date = inb[0]
            if city1['city_name'] == self.arrival_city and city1['price'] < self.price:
                client = Client(self.account_sid, self.auth_token)  # creates a Twilio client
                message = client.messages \
                    .create(
                    body=f"Low price alert! Only ${city1['price']} to fly from \n"
                         f" {self.departure_city_name}-{self.departure_airport_code} to {self.arrival_city}-"
                         f"{self.arrival_airport_code}, from \n"
                         f"{self.outbound_date} to {self.inbound_date}",
                    from_='+17146601370',  # here is a Twilio phone number
                    to='+*****'  # the phone number to which the message is to be sent
                )
                print(message.status)
                msg = f"Low price alert! Only ${city1['price']} to fly from {self.departure_city_name}-" \
                      f"{self.departure_airport_code} to {self.arrival_city}-{self.arrival_airport_code}, " \
                      f"from {self.outbound_date} to {self.inbound_date}."

                emails = [row["email"] for row in self.users]
                link = f"https://www.google.ca/flights?hl=en#flt={self.departure_airport_code}." \
                       f"{self.arrival_airport_code}.{self.outbound_date}*{self.arrival_airport_code}." \
                       f"{self.departure_airport_code}.{self.inbound_date} "

                self.send_emails(emails, msg, link)

    def send_emails(self, emails, message, flight_link):
        """Sends email to all users"""

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=email, to_addrs="******",
                                    msg=f"Subject:New Low "
                                        f"Price "
                                        f"Flight!\n\n"
                                        f"{message}\n"
                                        f"{flight_link}".encode('utf-8'))
