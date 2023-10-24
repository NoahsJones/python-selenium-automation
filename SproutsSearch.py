from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# open the url
driver.get('https://www.sprouts.com/')

#Pause the output
sleep(2)

# populate search field
#driver.find_element(By.XPATH, "//input[@placeholder='What can we help you find?']")

#Searching for an element on the page and then inputting value to it.
driver.find_element(By.XPATH, "//input[@placeholder='What can we help you find?']").send_keys('apple')

#Other way of searching for an element on the page and then inputting value to it. It is storing it in a variable
#search = driver.find_element(By.XPATH, "//input[@placeholder='What can we help you find?']")
# search.clear()
# search.send_keys('apple')

sleep(2)

driver.find_element(By.XPATH, "//button[@aria-label='Submit Search']").click()

sleep(2)

#Verification:
expected_result = 'Honeycrisp Apple (Avg. 0.4lb)'
actual_result = driver.find_element(By.XPATH, "//div[@title='Honeycrisp Apple (Avg. 0.4lb)']").text

#Test assertion:
assert expected_result == actual_result, f'Error, expected result "{expected_result}" did not match actual result "{actual_result}"'
print('Test Passed')

driver.quit()
