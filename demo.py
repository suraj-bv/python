from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "C:/path/to/chromedriver.exe"  # Update path here

try:
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    print("ChromeDriver is working!")
    driver.quit()
except Exception as e:
    print("ChromeDriver test failed:", e)
