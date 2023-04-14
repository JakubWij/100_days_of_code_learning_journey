import requests
import smtplib
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

#environmental variables
# export HIDDEN_API_KEY=------- NO SPACES
# in code os.environ.get("HIDDEN_API_KEY")

API_KEY = config['DEFAULT']['API_KEY']
MY_LAT = 51.107883 # Your latitude
MY_LONG = 17.038538 # Your longitude
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"
MY_EMAIL = config['DEFAULT']['my_email']
PASSWORD = config['DEFAULT']['password']


bendigo_lat = -36.759338
bendigo_lon = 144.283997


weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(url=OMW_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"][:4]

will_rain = False
for i in weather_list:
    # current_dict = i["weather"]
    current_id = i["weather"][0]["id"]
    if current_id <= 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg="Subject:It's going to rain today. Bring an umbrella")
