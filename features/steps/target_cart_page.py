from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_PRODUCT = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@then("target verify {product} in cart")
def verify_cart(context, product):
    # context.driver.wait.until(EC.visibility_of_element_located(CART_PRODUCT))
    # #sleep(4)
    # expected_result = product
    # actual_result = context.driver.find_element(*CART_PRODUCT).text
    # assert expected_result in actual_result, f"Error, expected {expected_result} but got this {actual_result}"
    context.app.cart_page.open_cart_page()
    context.app.cart_page.verify_product_in_cart(product)


@then("Message displays 'Cart is empty'")
def verify_cart_empty(context):
    sleep(0.2)
    context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your cart is empty']")))
    # expected_result = 'cart is empty'
    # actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    # assert expected_result in actual_result, (f'Error, the expected "{expected_result}" was not the same as'
    #                                           f'actual "{actual_result}"')
    context.app.cart_page.verify_cart_empty()