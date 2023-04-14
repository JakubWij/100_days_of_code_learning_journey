import requests
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

USERNAME = config['DEFAULT']['USERNAME']
TOKEN = config['DEFAULT']['TOKEN']
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#create user account in pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Graph",
    "unit": "min",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#post a pixel

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#to create from yestedray
# today = datetime(year=2022, month=10, day=15)
# print(today)

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}
response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(response.text)

# update pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "30"
}
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# delete pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
