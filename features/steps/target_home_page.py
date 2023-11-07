from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

'''Always put 'context.driver.'etc....'''
@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)


@when('Click on Cart icon')
def click_on_cart(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(2)


@when('Under navigation menu, click sign in')
def click_navigation_menu_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in' and @class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
    sleep(2)


@then("Verify header is present")
def header_is_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")

@then("Verify header has {number} links")
def header_has_links(context, number):
    number = int(number)
    header_links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(header_links) == number, f"Error, expected {number} links but got actually {len(header_links)} links"