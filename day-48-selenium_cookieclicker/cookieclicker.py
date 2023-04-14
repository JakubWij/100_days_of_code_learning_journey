from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from threading import Timer


chrome_driver_path = "D:\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
# get cookie
cookie = driver.find_element(By.ID, "cookie")
# get item upgrade id
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]

money = driver.find_element(By.ID, "money").text


# costs_dictionary = {
#     "cursor": cursor_cost,
#     "grandma": grandma_cost,
#     "factory": factory_cost,
#     "mine": mine_cost,
#     "shipment": shipment_cost
# }
timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes


while True:
    cookie.click()
    # every 5 seconds
    if time.time() > timeout:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]

        # get cookie current count
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        money_amount = int(money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money_amount > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]


        purchase_id = driver.find_element(By.ID, to_purchase_id).click()


        #Add another 5 seconds until the next check
        timeout = time.time() + 5
    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break




