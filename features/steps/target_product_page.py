from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("target add coffee to cart")
def add_product(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[alt='Folgers Classic Medium Roast Ground Coffee']").click()
    sleep(2)
    context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor13397813").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()
    sleep(4)


@then('Verify search worked for {product}')
def verify_search(context, product):
    expected_result = product
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert expected_result in actual_result, f"Error, expected {expected_result} is not in actual '{actual_result}'"
    sleep(2)



@then('Verify {product} in search result url')#This is the And in the feature file
def verify_search_url(context, product):
    sleep(2)
    assert product in context.driver.current_url


@then("target verify {product_result} is found")
def verify_product_search(context, product_result):
    expected_result = product_result
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), product_result)]").text
    assert expected_result in actual_result, f"Error, expected {expected_result} and got this {actual_result} instead"