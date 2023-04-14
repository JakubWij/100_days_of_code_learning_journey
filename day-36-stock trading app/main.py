# CURRENTLY NOT WORKING BECAUSE ALPHAVANTAGE CHANGED THEIR SERVICE FROM FREE TO PREMIUM
import requests
import smtplib
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = config['DEFAULT']['STOCK_API_KEY']
NEWS_API_KEY = config['DEFAULT']['NEWS_API_KEY']

MY_EMAIL = config['DEFAULT']['MY_EMAIL']
PASSWORD = config['DEFAULT']['PASSWORD']

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']
close_list = [value["4. close"] for (key, value) in stock_data.items()]
yesterday_value = float(close_list[:1][0])

day_before_value = float(close_list[:2][1])

positive_difference = yesterday_value - day_before_value
up_down =None
if positive_difference > 0:
    up_down = "+"
else:
    up_down = "-"


# percentage_diff = round((abs(yesterday_value / day_before_value) * 100) - 100, 2)
percentage_diff = round(((positive_difference / yesterday_value) * 100), 2)
print(percentage_diff)
# print(yesterday_value)
# print(day_before_value)
# print(percentage_diff)
if abs(percentage_diff) > 1:
    news_params = {
        "q": COMPANY_NAME,
        "from": list(stock_data.keys())[0], # acces all keys from dict change to list and take 1st item of list
        "to": list(stock_data.keys())[0],
        "sortBy": "popularity",
        "apikey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_list = news_response.json()["articles"][:3]

    headline_list = [value["title"] for value in news_list]
    description_list = [value["description"] for value in news_list]
    # formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_list]
# send via mail
    connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:Tesla Stock trading\n\n{COMPANY_NAME}{percentage_diff}\n"
                            f"Headline1:{headline_list[0].encode('ascii', 'ignore')}\nBrief1:{description_list[0].encode('ascii', 'ignore')},\n\n"
                            f"Headline2:{headline_list[1].encode('ascii', 'ignore')}\nBrief2:{description_list[1].encode('ascii', 'ignore')},\n\n"
                            f"Headline3:{headline_list[2].encode('ascii', 'ignore')}\nBrief3:{description_list[2].encode('ascii', 'ignore')},\n\n"
                        )

