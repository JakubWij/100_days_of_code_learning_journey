# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from notification_manager import NotificationManager
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
print(config['DEFAULT']['apikey'])
print(config['DEFAULT']['Authorization'])

MY_MAIL = config['DEFAULT']['MY_MAIL']
PASSWORD = config['DEFAULT']['PASSWORD']

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for destination in sheet_data:
        destination["iataCode"] = flight_search.get_destination_code(destination["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_data()

for destination in sheet_data:
    # print(destination)
    flight = flight_search.search_flight(city_code=destination["iataCode"], max_stopovers=2)
    if flight is None:
        continue
    if flight.stop_overs > 1:
        print(f"Flight has {flight.stop_overs} stop overs, via"
              f" {', '.join(flight.via_city[:-1]) + ' and ' + flight.via_city[-1]}.")
    elif flight.stop_overs > 0:
        print(f"Flight has {int(flight.stop_overs)} stop over, via {flight.via_city[0]}.")
    if destination["lowestPrice"] > flight.price:
        notification = NotificationManager(MY_MAIL, PASSWORD, *flight)
        notification.send_mail()


print("""Welcome to James's Flight Club.\nWe find the best flight deals and email you.""")
f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
email = input("What is your email\n")
email_validation = input("Type your email again.\n")
if email == email_validation:
    data_manager.user_data(email,f_name,l_name)
    print("You're in the club!")
