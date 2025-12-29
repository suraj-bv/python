# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://amazon.com")
# print(driver.title)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get("https://accounts.google.com/")

# email_input = driver.find_element(By.ID, "identifierId")
# email_input.send_keys("your_email@gmail.com")
# driver.find_element(By.ID, "identifierNext").click()

# time.sleep(3)

# password_input = driver.find_element(By.NAME, "password")
# password_input.send_keys("your_password")
# driver.find_element(By.ID, "passwordNext").click()

# # Wait and quit
# time.sleep(10)
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()
# driver.get("https://accounts.google.com/")

# email_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "identifierId"))
# )
# email_input.send_keys("your_email@gmail.com")
# driver.find_element(By.ID, "identifierNext").click()

# password_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "password"))
# )
# password_input.send_keys("your_password")
# driver.find_element(By.ID, "passwordNext").click()

# time.sleep(10)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()
# driver.get("https://accounts.google.com/")

# try:
#     email_input = WebDriverWait(driver, 15).until(
#         EC.visibility_of_element_located((By.ID, "identifierId"))
#     )
#     email_input.send_keys("surajbv1122@gmail.com")
#     driver.find_element(By.ID, "identifierNext").click()

#     password_input = WebDriverWait(driver, 15).until(
#         EC.visibility_of_element_located((By.NAME, "Passwd"))  # Correct field name
#     )
#     password_input.send_keys("@PunkBabe0710")
#     driver.find_element(By.ID, "passwordNext").click()

#     time.sleep(10)

# except Exception as e:
#     print("Error occurred:", e)
#     driver.save_screenshot("error_screenshot.png")

# finally:
#     driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
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
time
driver.quit()
