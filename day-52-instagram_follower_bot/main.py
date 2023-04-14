from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
INSTAGRAM_MAIL = config['DEFAULT']['INSTAGRAM_MAIL']
INSTAGRAM_PASSWORD = config['DEFAULT']['INSTAGRAM_PASSWORD']
CHROME_DRIVER_PATCH = "D:\Python\chromedriver.exe"
ACCOUNT_TO_FOLLOW = "python.hub"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATCH)

    def login(self):
        instagram_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url=instagram_url)
        time.sleep(5)
        # cookies
        self.driver.find_element(By.CLASS_NAME, "_a9_1").click()
        self.driver.find_element(By.NAME, "username").send_keys(INSTAGRAM_MAIL)
        self.driver.find_element(By.NAME, "password").send_keys(INSTAGRAM_PASSWORD)
        time.sleep(3)
        # click login
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button').click()
        time.sleep(7)
        # save login data-deny
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        # anouncements off
        self.driver.find_element(By.CLASS_NAME, '_a9_1').click()
        time.sleep(2)

    def find_followers(self):
        # pass keys to search bar
        search_bar = self.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(ACCOUNT_TO_FOLLOW)
        time.sleep(5)
        search_bar.send_keys(Keys.ENTER)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)
        # click on observers
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)
        popup_window_followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup_window_followers)
            time.sleep(2)


    def follow(self):
        num = 1
        while True:
            try:
                self.driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{num}]/div[3]/button").click()
                time.sleep(1)
            except ElementClickInterceptedException: # exception for someone I followed already
                self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
                time.sleep(1)
            except NoSuchElementException: # additional exception for antibot
                time.sleep(100)
            num += 1
            print(num)
'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/button'
'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[3]/button'

follower_bot = InstaFollower()
follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()
time.sleep(1000)
