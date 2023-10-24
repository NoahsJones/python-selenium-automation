from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Installing the driver path:
driver_path = ChromeDriverManager().install()

#Setting up the chrome browser to use and create an instance of it:
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#Getting the URL of the site to navigate to:
driver.get('https://www.target.com/')

sleep(2)

driver.find_element(By.ID, "search").send_keys("Christmas Decorations")
driver.find_element(By.XPATH, "//button[@aria-label='search']").click()

sleep(4)

driver.find_element(By.XPATH, "//*[contains(text(), 'Christmas')]")

sleep(2)

expected_result = '“Christmas Decorations”'
actual_result = driver.find_element(By.XPATH, "//span[@class='h-margin-r-x2']").text

'''Checking to see if the string value stored in expected result is ever found in the actual web page element. If true the
 program will continue and then the print function will call'''
assert expected_result in actual_result, f"Error, '{expected_result}' was not found on the page. Found '{actual_result}' instead."
print(f"Test Passed: '{expected_result}' was found on the page.")







