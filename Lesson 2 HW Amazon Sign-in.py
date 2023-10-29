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

expected_result_1 = 'Create your Amazon account'
actual_result_1 = driver.find_element(By.ID, 'createAccountSubmit').text

assert expected_result_1 == actual_result_1, f"Error, '{expected_result_1}' is not the same as '{actual_result_1}'."
print("Test Case 1: Passed")

'''This test verification is fine too. I do not need to reupload and do not need to resubmit my hw. This was good'''
expected_result_2 = "Email or mobile phone number"
actual_result_2 = driver.find_element(By.XPATH, "//label[@for='ap_email']").text

assert expected_result_2 == actual_result_2, f"Error, '{expected_result_2}' is not the same as '{actual_result_2}'."
print("Test Case 2: Passed")

'''This is not needed for the hw this is just for education:'''
driver.find_element(By.ID, 'ap_email')
print("Test Case 3: Passed")

'''Not a part of the hw this below test:'''
expected_result_3 = "Conditions of Use and Privacy Notice."
actual_result_3 = driver.find_element(By.ID, 'legalTextRow').text
assert expected_result_3 in actual_result_3, f'Expected {expected_result_3} did not match actual {actual_result_3}'
print("Test Case 4: Passed")

driver.quit()