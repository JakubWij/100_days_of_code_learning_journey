import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

target_price = 220

url_en = "https://www.amazon.com/AMD-5700X-16-Thread-Unlocked-Processor/dp/B09VCHQHZ6/ref=sr_1_2?keywords=ryzen+7+5800x" \
         "&qid=1668262267&sprefix=ryzen+7+580%2Caps%2C192&sr=8-2"

params_en = {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
      "Accept-Language": "en-US"
}

response = requests.get(url=url_en, headers=params_en)
amazon_web_page = response.text


soup = BeautifulSoup(amazon_web_page, "lxml")
price = soup.find(name="span", class_="a-price-whole").getText()
price_as_float = float(price)
product_title = soup.find(id="productTitle").getText().strip()


# connect to smtplib
if price_as_float < target_price:
    my_email = config['DEFAULT']['my_email']
    password = config['DEFAULT']['password']

    connection = smtplib.SMTP("smtp.gmail.com", port=587, timeout=120)
    connection.starttls()
    connection.login(user=my_email, password=password)
    msg = f"Subject: Amazon price alert!\n\n{product_title} is now ${price_as_float}\n{url_en}"
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.encode("utf8"))

