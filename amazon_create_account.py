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
driver.get('https://www.amazon.com/')

sleep(2)

#Navigate to the sign-in page:
driver.find_element(By.ID, 'nav-orders').click()

sleep(2)

#Find button to navigate to create account page:
driver.find_element(By.ID, "createAccountSubmit").click()

sleep(3)

#Find webpage elements on the create account page:
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "ap_password")
driver.find_element(By.XPATH, "//div[contains(text(), '6 characters')]")
driver.find_element(By.ID, "ap_password_check")
driver.find_element(By.ID, "continue")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin?showRmrMe']")

#Verification message:
print('Test case passed: all web elements found on account creation page')
