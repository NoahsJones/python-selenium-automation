from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Sign in form opened')
def verify_sign_in(context):
    expected_result = 'Sign into'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Error, expected {expected_result} does not match actual {actual_result}'