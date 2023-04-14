from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_patch = "D:\Python\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_patch)
        self.promised_up_speed = 1
        self.promised_down_speed = 10
        self.up_speed = 0
        self.down_speed = 0

    def get_internet_speed(self):
        speed_test_url = "https://www.speedtest.net"
        self.driver.get(url=speed_test_url)
        time.sleep(3)
        # click accept privacy
        self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()
        # start test
        self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a").click()
        time.sleep(45)
        # find and print both up and down speed
        self.down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down_speed)
        print(self.up_speed)
        self.driver.close()
        time.sleep(5)

    def tweet_at_provider(self):
        twitter_mail = config['DEFAULT']['twitter_mail']
        twitter_password = config['DEFAULT']['twitter_password']
        twitter_username = config['DEFAULT']['twitter_username']
        self.driver = webdriver.Chrome(executable_path=self.chrome_patch)
        twitter_url = "https://twitter.com"
        self.driver.get(url=twitter_url)
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a').click()
        time.sleep(5)
        twitter_login_mail = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        twitter_login_mail.send_keys(twitter_mail)
        twitter_login_mail.send_keys(Keys.ENTER)
        time.sleep(5)
        twitter_login_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        twitter_login_username.send_keys(twitter_username)
        twitter_login_username.send_keys(Keys.ENTER)
        time.sleep(5)
        twitter_login_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        twitter_login_password.send_keys(twitter_password)
        twitter_login_password.send_keys(Keys.ENTER)
        # then tweet at someone but im too lazy to do the same thing over and over again its easy
        time.sleep(500)

