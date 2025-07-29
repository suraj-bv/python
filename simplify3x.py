from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_preference("dom.webnotifications.enabled", False)

service = Service(executable_path="D:\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://accounts.google.com/")

email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys("demoemailid@gmail.com")
driver.find_element(By.ID, "identifierNext").click()

try:
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("qwerty@13579")
    driver.find_element(By.ID, "passwordNext").click()
except:
    print("Password field not found")

time.sleep(10)
driver.quit()
