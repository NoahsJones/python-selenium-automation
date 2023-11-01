from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open sprouts main page')
def open_sprouts(context):
    context.driver.get('https://www.sprouts.com/')
    sleep(2)

@when('sprouts search product')
def search_product(context):
    context.driver.find_element(By.XPATH, "//input[@type='search']").send_keys('cereal')
    sleep(2)
    context.driver.find_element(By.XPATH, "//button[@aria-label='Submit Search']").click()
    sleep(15)

@when('sprouts select the product')
def select_product(context):
    context.driver.find_element(By.XPATH, "//div[@title='Cascadian Farm Organic Cinnamon Crunch Cereal']").click()
    sleep(2)

@when('sprouts add product to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-quantity-button']").click()
    sleep(2)

@when('sprouts navigate to cart')
def navigate_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='modal-close-button']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Open cart: There are 1 items in your list']").click()
    sleep(2)

@then('sprouts verify product is in cart')
def verify_product(context):
    expected_result = 'Cinnamon Crunch Cereal'
    actual_result = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Cinnamon Crunch']")
    assert expected_result in actual_result, f'Error, the expected "{expected_result} is not the same as actual "{actual_result}"'
    sleep(2)





