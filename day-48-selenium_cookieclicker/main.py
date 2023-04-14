from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "D:\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://www.python.org")

# filling in internet forms
# search_bar = driver.find_element(By.ID, "id-search-field")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = (driver.find_elements(By.CSS_SELECTOR, ".documentation-widget a "))
# print(documentation_link[0].text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

menu = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# print(menu)
# //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]
# //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]
dictionary = {}
counter = 1
for obj in range(5):
    event_obj = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{counter}]')
    event_obj_list = event_obj.text.split("\n")
    dictionary[f"{counter-1}"] = {f"{event_obj_list[0]}": f"{event_obj_list[1]}"}
    counter += 1

print(dictionary)
driver.quit()
