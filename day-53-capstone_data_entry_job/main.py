import requests
from bs4 import BeautifulSoup
import pprint
import random

params_en = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US"
}

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSePAAr65C8s41OjmdVYNr83YhMC4ZzT3l78ThWqqyHIPQ4row/viewform?usp=sf_link"
zillow_url = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"%3A-122.68910445166016%2C"east"%3A-122.17755354833984%2C"south"%3A37.61555442082665%2C"north"%3A37.934684099448255%7D%2C"mapZoom"%3A11%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D'

response = requests.get(url=zillow_url, headers=params_en)
site = response.text
soup = BeautifulSoup(site, "html.parser")

listings_href = soup.find_all(name="a",
                              class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link')

href_list = []
for listing in listings_href:
    if "zillow" not in listing.get("href"):
        href = f'https://www.zillow.com/{listing.get("href")}'
    else:
        href = listing.get('href')
    href_list.append(href)

address_list = [listing.getText().split(" | ")[-1] for listing in listings_href]

listing_price = soup.find_all(name="div",
                              class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX")

price_list = [listing.getText().split('+')[0] for listing in listing_price]
# for listing in listing_price:
#       print(listing.getText().split('+')[0])
print(price_list)



