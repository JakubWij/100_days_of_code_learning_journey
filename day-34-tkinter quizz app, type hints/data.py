import requests


URL = "https://opentdb.com/api.php"
URL2 = "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium&type=boolean"


parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "medium",
}
response = requests.get(url=URL, params=parameters)
# response = requests.get(url=URL2)
response.raise_for_status()
data = response.json()
question_data = data["results"]

