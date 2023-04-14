from math import floor
import requests
import datetime
from flight_data import FlightData
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = {
    "apikey": config['DEFAULT']['apikey']}
WROCLAW_CODE = "WRO"
LONDON_CODE = "LON"
TOMORROW_DATE = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
MAX_DATE = (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        api_params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=api_params, headers=TEQUILA_API_KEY)
        code = response.json()["locations"][0]["code"]
        return code

    def search_flight(self, city_code, max_stopovers=0):
        api_params = {
            "fly_from": LONDON_CODE,
            "fly_to": city_code,
            "date_from": TOMORROW_DATE,
            "date_to": MAX_DATE,
            "curr": "GBP",
            # "price_to": price,
            "max_stopovers": max_stopovers,
            "flight_type": "round",
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 27,
            "one_for_city": 1,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=api_params, headers=TEQUILA_API_KEY)

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for {city_code}")
            return None
        else:
            via_city = []
            if len(data["route"]) / 2 - 1 > 0:
                for flight in data["route"][:int(len(data["route"]) / 2 - 1)]:
                    via_city.append(flight["cityTo"])
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=floor(len(data["route"]) / 2 - 1),
                via_city=via_city
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")

            return flight_data
