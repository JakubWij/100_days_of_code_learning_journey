from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

TEL = config['DEFAULT']['TEL']
PASSWORD = config['DEFAULT']['PASSWORD']
URL = "https://tinder.com/"
CHROME_PATCH = "D:\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_PATCH)
driver.get(URL)
main_page = driver.current_window_handle
driver.maximize_window()
time.sleep(5)
# click login
login_button = driver.find_element(By.XPATH, '//*[@id="s-1602360476"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(3)
# continue using facebook
continue_facebook = driver.find_element(By.CSS_SELECTOR, "#q-929574956 > main > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3) > span > div:nth-child(2) > button")
continue_facebook.click()
window_before = driver.window_handles[0]
time.sleep(3)
# cookie accept, swap windows
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
cookie_accept_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]').click()


# email, password pass in
tel = driver.find_element(By.XPATH, '//*[@id="email"]')
tel.send_keys(TEL)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)
fb_login_btn = driver.find_element(By.ID, "loginbutton")
fb_login_btn.click()
# swap windows
driver.switch_to.window(window_before)
time.sleep(8)
print(driver.title)
# allow gps
allow_gps_btn = driver.find_element(By.XPATH, '//*[@id="q-929574956"]/main/div/div/div/div[3]/button[1]').click()
time.sleep(5)
# # disallow pop-ups
disallow_popups_btn = driver.find_element(By.XPATH, '//*[@id="q-929574956"]/main/div/div/div/div[3]/button[2]').click()
time.sleep(2)
# privacy pop-up disallow
privacy_popup_btn = driver.find_element(By.XPATH, '//*[@id="q798806120"]/div/div[2]/div/div/div[1]/div[2]/button').click()
# dark mode disallow
dark_mode_popup = driver.find_element(By.XPATH, '//*[@id="q-929574956"]/main/div/div[2]/button').click()

# like people
while True:
    try:
        hit_like_btn = driver.find_element(By.CSS_SELECTOR, '#q798806120 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button').click()
        time.sleep(1)
    except NoSuchElementException:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button[2]').click()
        finally:
            time.sleep(2)
            continue
    except ElementClickInterceptedException:
        # match! dismiss xdd go next
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="q1129177321"]/main/div/div[1]/div/div[4]/button').click()
        time.sleep(1)
        continue

time.sleep(300)


