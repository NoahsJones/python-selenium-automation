from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("target search for {product}")
def search_product(context, product):
    context.driver.find_element(By.ID, "search").send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(2) #Cannot find alternative for sleep

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, "search").send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()
    sleep(3)  #Cannot find alternative for sleep