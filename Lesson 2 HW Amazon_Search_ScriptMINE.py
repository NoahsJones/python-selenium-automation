from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Getting the drivers installed from selenium for chrome and opening the browser:
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

#Maximize the window to full screen:
driver.maximize_window()

#Stop execution of code for however many seconds:
sleep(2)

#Navigate to the amazon site:
driver.get('https://www.amazon.com/')

#Finding the search bar and inputting some string value into the field:
driver.find_element(By.ID, "twotabsearchtextbox").send_keys('mug')

#Find and Clicking on search button to execute search criteria:
driver.find_element(By.ID, "nav-search-submit-button").click()

sleep(2)

expected_result = '"mug"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result, f"Error, {expected_result} is not the same as {actual_result}"
print("Test case passed.")

