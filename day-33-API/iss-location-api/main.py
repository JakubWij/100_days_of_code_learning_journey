import requests
from datetime import datetime
import smtplib
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


MY_LAT = 51.107883 # Your latitude
MY_LONG = -17.038538 # Your longitude
MY_EMAIL = config['DEFAULT']['my_email']
PASSWORD = config['DEFAULT']['password']


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunrise_hour < time_now.hour or sunset_hour > time_now.hour:
        return True
    else:
        return False


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if 5 >= MY_LAT - iss_latitude >= -5 and 5 >= MY_LONG - iss_longitude >= -5:
        return True
    else:
        return False


# If the ISS is close to my current position,
# and it is currently dark
# while True:
#     time.sleep(60)
#     if is_iss_close() and is_dark():
#         # Then email me to tell me to look up.
#         # gmail connection
#         connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=MY_EMAIL,
#                             msg="Subject:Iss above head")

# BONUS: run the code every 60 seconds.

connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)
connection.sendmail(from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject:Iss above head")