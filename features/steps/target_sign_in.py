from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(2)


@when('Under navigation menu, click sign in')
def click_navigation_menu_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in' and @class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
    sleep(2)

@then('Sign in form opened')
def verify_sign_in(context):
    expected_result = 'Sign into'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Error, expected {expected_result} does not match actual {actual_result}'