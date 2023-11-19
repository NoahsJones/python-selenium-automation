from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_FIELD = By.ID, "search"
SEARCH_BTN = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"

@when("target search for {product}")
def search_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(2) #Cannot find alternative for sleep
    context.app.main_page.search(product)

@when('Search for {product}')
def search_product(context, product):
    # context.driver.find_element(By.ID, "search").send_keys(product)
    # context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()
    # sleep(3)  #Cannot find alternative for sleep
    context.app.main_page.search(product)