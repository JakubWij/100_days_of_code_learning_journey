# URL = "https://replit.com/@JackobWave/day-38#main.py"

import os
from datetime import datetime
import requests

GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 174
AGE = 24

NUTRITIONX_API_KEY = os.environ['NUTRITIONX_API_KEY']
NUTRITIONX_ID = os.environ['NUTRITIONX_ID']
MAIL = os.environ['MAIL']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']


sheety_api = os.environ['sheety_api']
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
    "Authorization": os.environ['Bearer'],
}
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# post needs data= where get needs params=
response = requests.post(url=nutritionx_api_endpoint, data=nutrition_params, headers=nutri_headers)
result = response.json()
print(result)
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

