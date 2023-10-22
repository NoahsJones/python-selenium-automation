from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


'''Test Case: Logged out user sees Sign in page when clicking Orders'''


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

sleep(2)

#Navigate to the sign-in page:
driver.find_element(By.ID, 'nav-orders').click()

sleep(2)

#Finding the elements visible on page initially:
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//input[@name='email']")
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.ID, 'createAccountSubmit')

sleep(2)

#Opening the dropdown for Need Help:
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-expand']").click()

sleep(2)

#Finding the elements in Need Help drop-down:
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID, 'ap-other-signin-issues-link')

sleep(2)


expected_result_1 = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
actual_result_1 = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

assert expected_result_1 == actual_result_1, "Error, the sign in page did not open."
print("Test Case 1: Passed")


expected_result_2 = driver.find_element(By.ID, 'ap_email')
actual_result_2 = driver.find_element(By.ID, 'ap_email')

assert expected_result_2 == actual_result_2, "Error, there is no email field"
print("Test Case 2: Passed")




driver.quit()