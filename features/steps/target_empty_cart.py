from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Cart icon')
def click_on_cart(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then("Message displays 'Cart is empty'")
def verify_cart_empty(context):
    sleep(2)
    expected_result = 'cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_result in actual_result, (f'Error, the expected "{expected_result}" was not the same as'
                                              f'actual "{actual_result}"')

