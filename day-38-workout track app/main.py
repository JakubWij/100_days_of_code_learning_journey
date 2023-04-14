from datetime import datetime
import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 174
AGE = 24

NUTRITIONX_API_KEY = config['DEFAULT']['NUTRITIONX_API_KEY']
NUTRITIONX_ID = config['DEFAULT']['NUTRITIONX_ID']
MAIL = config['DEFAULT']['MAIL']
MAIL_PASSWORD = config['DEFAULT']['MAIL_PASSWORD']

sheety_api = "https://api.sheety.co/3ea398dabf0ce94433f9d0296d983153/pythonWorkoutsSheet/workouts"
nutritionx_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_headers = {
    "x-app-id": NUTRITIONX_ID,
    "x-app-key": NUTRITIONX_API_KEY
}
nutrition_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
sheety_headers = {
    "Authorization": "Bearer AAAAAAMLheAAAAAAA0%2Bfbalkwfudnw45962jvm57g30iRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F",
}
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# post needs data= where get needs params=
response = requests.post(url=nutritionx_api_endpoint, data=nutrition_params, headers=nutri_headers)
result = response.json()
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=sheety_api, json=sheet_inputs, headers=sheety_headers)

print(response.text)

