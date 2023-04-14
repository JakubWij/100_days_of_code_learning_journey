from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3354927596&f_AL=true&f_E=1%2C2&f_WRA=true&geoId=105072130&keywords=python%20developer&location=Polska&refresh=true&sortBy=R"
EMAIL = config['DEFAULT']['EMAIL']
PASSWORD = config['DEFAULT']['PASSWORD']


chrome_patch_driver = "D:\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_patch_driver)
driver.get(url=URL)

# find login button and click
login_button = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
login_button.click()

# pass login data
mail_form = driver.find_element(By.ID, "username")
mail_form.send_keys(EMAIL)
password_form = driver.find_element(By.ID, "password")
password_form.send_keys(PASSWORD)
second_login_button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
second_login_button.click()
# wait for web to load
time.sleep(5)

# after login click on one aplication and apply
easy_apply_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button')
easy_apply_button.click()
# dalej
time.sleep(5)
next_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
next_button.click()
time.sleep(5)
next_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next_button.click()


while True:
    time.sleep(300)

