# count = [0] * 10
# print(count)

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://amazon.com")
# print(driver.title)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Set up the WebDriver
# driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
# driver.get("https://accounts.google.com/")

# # Enter email
# email_input = driver.find_element(By.ID, "identifierId")
# email_input.send_keys("your_email@gmail.com")  # Replace with your Gmail
# driver.find_element(By.ID, "identifierNext").click()

# time.sleep(3)

# # Enter password
# password_input = driver.find_element(By.NAME, "password")
# password_input.send_keys("your_password")  # Replace with your password
# driver.find_element(By.ID, "passwordNext").click()

# # Wait and quit
# time.sleep(10)
# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.get("https://accounts.google.com/")

# Enter email
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)
email_input.send_keys("your_email@gmail.com")  # Replace with your Gmail
driver.find_element(By.ID, "identifierNext").click()

# Wait for the password field to appear
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys("your_password")  # Replace with your password
driver.find_element(By.ID, "passwordNext").click()

# Optional: wait and quit
time.sleep(10)
driver.quit()
