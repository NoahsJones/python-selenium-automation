from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

'''Always put 'context.driver.'etc....'''
@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_product(context):
    context.driver.find_element(By.ID, "search").send_keys('spicy chip')
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()
    sleep(3)


@then('Verify search worked')
def verify_search(context):
    expected_result = "spicy chip"
    actual_result = context.driver.find_element(By.XPATH, "//span[contains(text(),'“spicy chip”')]").text
    assert expected_result in actual_result, f"Error, expected {expected_result} is not in actual '{actual_result}'"
    sleep(2)


@then('Verify search result url')#This is the And in the feature file
def verify_search_url(context):
    assert 'spicy' in context.driver.current_url
