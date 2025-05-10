from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image, ImageChops

options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)

options.add_argument(f'--user-agent={user_agent}')
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://marvelcinematicuniverse.fandom.com/wiki/Rocket_Raccoon")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1920, total_height)

actual_image_path = "rocket_raccoon.png"
expected_image_path = "expected.png"
result_destination = "result.png"

driver.save_screenshot(actual_image_path)

time.sleep(5)
driver.quit()

expected_image = Image.open(expected_image_path).convert("RGB")
actual_image = Image.open(actual_image_path).convert("RGB")

diff = ImageChops.difference(expected_image, actual_image)

if diff.getbbox():
    diff.save(result_destination)
    print("Image are different:", result_destination)
else:
    print("Images the same.")
