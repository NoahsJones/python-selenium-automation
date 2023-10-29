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


#Search using ID in CSS
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
#Search using ID in CSS using tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
#Search by CSS using one class:
driver.find_element(By.CSS_SELECTOR, '.nav-input')
#Search by CSS using two classes:
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute')
#Search by CSS using multiple classes:
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')
#Search by CSS using tag + two classes:
driver.find_element(By.CSS_SELECTOR, 'input.nav-input.nav-progressive-attribute')
#Search by CSS using tag + ID + two classes:
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-input.nav-progressive-attribute')
#Search by CSS using attributes:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][dir='auto']")
#Search by CSS using tag + attributes:
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][dir='auto']")
#Search by CSS using tag + class + attributes:
driver.find_element(By.CSS_SELECTOR, "input.nav-input[placeholder='Search Amazon'][dir='auto']")
#Search by CSS using tag + ID + class + attributes:
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][dir='auto']")
#Search by CSS using attribute with '*' for contains that value in something:
driver.find_element(By.CSS_SELECTOR, "[data-csa-c-content-id*='nav_cs_bestsellers']")

#Search by CSS finding multiple elements (Parent to child only) separated by a space ' ':
driver.find_element(By.CSS_SELECTOR, "#nav-main a[href*='holdeals_ranked']")
