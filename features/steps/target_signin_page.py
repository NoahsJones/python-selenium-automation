from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given("target Open sign in page")
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when("Click on Target terms and conditions link")
def click_on_terms_conditions(context):
    context.app.sign_in_page.click_terms_conditions()


@when("Store original windows") #Just a copy of the original class code from target_circle_page steps. But I wrote this for hw
def store_original_window(context):
    context.windows_list = context.app.page.get_all_windows()
    context.origin_window = context.app.page.get_current_window()


@when("Switch to the newly opened window") #Just a copy of the original class code from target_circle_page steps. But I wrote this for hw
def switch_windows(context):
    context.app.page.switch_to_new_window()


@then("Verify Terms and Conditions page is opened")
def verify_terms_conditions_opened(context):
    context.app.sign_in_page.verify_terms_conditions_opened()


@then("User can close new window and switch back to original")
def close_window(context):
    context.app.page.close_page()
    #sleep(2)
    context.app.page.switch_to_window(context.origin_window)





@then('Sign in form opened')
def verify_sign_in(context):
    # context.driver.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[text()='Sign into your Target account']"), 'Sign into'))
    # expected_result = 'Sign into'
    # actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    # assert expected_result in actual_result, f'Error, expected {expected_result} does not match actual {actual_result}'
    context.app.sign_in_page.verify_on_sign_in_page()


@when("Input user credentials email: {email} password: {password}")
def input_credentials(context, email, password):
    context.app.sign_in_page.log_in(email, password)