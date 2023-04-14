from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "D:\Python\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
#
# wiki_articles_num = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # wiki_articles_num.click()
#
# # clicking link text (blue text on stite)
# commons = driver.find_element(By.LINK_TEXT, "Commons")
# # commons.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# #################### newsletter ###################
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://secure-retreat-92358.herokuapp.com")

f_name = driver.find_element(By.CLASS_NAME, "top")
f_name.send_keys("werer")
l_name = driver.find_element(By.CLASS_NAME, "middle")
l_name.send_keys("werer")
mail = driver.find_element(By.CLASS_NAME, "bottom")
mail.send_keys("werer@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

time.sleep(5000)

