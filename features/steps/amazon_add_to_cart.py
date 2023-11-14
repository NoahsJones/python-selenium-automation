from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('open amazon main page')
def amazon_main_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(3)


@when('amazon search product')
def amazon_search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('flashlight')
    sleep(2)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    sleep(2)


@when('amazon select the product')
def amazon_select_product(context):
    context.driver.find_element(By.XPATH, "//img[@alt='ALSTU Rechargeable Flashlights High Lumens, 299000 Lumen Bright Flashlight with 5 Modes, Led Flash Light with Power Display & IPX7 Waterproof for Camping, Hiking, Outdoor (2 Packs)']").click()
    sleep(2)

@when('amazon add product to cart')
def amazon_add_product(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.driver.find_element(By.CSS_SELECTOR, "input.a-button-input[type='submit'][aria-labelledby='attachSiNoCoverage-announce']").click()
    sleep(2)


@when('amazon navigate to cart')
def amazon_navigate_to_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
    sleep(2)


@then('amazon verify product is in cart')
def amazon_verify_product_in_cart(context):
    expected_result = '1'
    actual_result = context.driver.find_element(By.ID, "sc-subtotal-label-buybox").text
    assert expected_result in actual_result, f"Error, expected '{expected_result} is not the same as actual {actual_result}"
