import requests
from pprint import pprint
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        # if authorization key in configparser contain % we must change it to %% to escape it
        self.sheety_token = {
            'Authorization': config["DEFAULT"]['Authorization']
        }
        self.sheety_prices_endpoint = "https://api.sheety.co/c43b699fdb0992c7ebb36854e0632733/pythonFlightDeals/prices"
        self.sheety_users_endpoint = "https://api.sheety.co/c43b699fdb0992c7ebb36854e0632733/pythonFlightDeals/users"

    def get_data(self):
        data = requests.get(url=self.sheety_prices_endpoint, headers=self.sheety_token).json()
        print(data)
        # data ={'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
        #                 {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
        #                 {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
        #                 {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
        #                 {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
        #                 {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
        #                 {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
        #                 {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
        #                 {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            sheet_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.sheety_prices_endpoint}/{city['id']}",
                                    headers=self.sheety_token,
                                    json=sheet_data)
            # print(response.text)

        # update = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/3", headers=SHEETY_TOKEN, json=self.destination_data)

    def user_data(self, users_mail, users_f_name, users_l_name):
        new_user_data = {
            "user": {
                "firstName": users_f_name,
                "lastName": users_l_name,
                "email": users_mail
            }
        }
        response = requests.post(url=self.sheety_users_endpoint, headers=self.sheety_token, json=new_user_data)
        print(response.text)

