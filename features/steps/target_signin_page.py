from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Sign in form opened')
def verify_sign_in(context):
    context.driver.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[text()='Sign into your Target account']"), 'Sign into'))
    expected_result = 'Sign into'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Error, expected {expected_result} does not match actual {actual_result}'