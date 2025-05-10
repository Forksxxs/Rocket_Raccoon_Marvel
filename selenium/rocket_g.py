from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)

options.add_argument(f'--user-agent={user_agent}')
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Rocket Raccoon - Marvel" + Keys.ENTER)

input("Pause for manual captcha and enter here")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Rocket Raccoon - Marvel"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Rocket Raccoon - Marvel")
link.click()

time.sleep(10)
driver.quit()