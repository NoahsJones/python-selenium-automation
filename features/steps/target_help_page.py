from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given("Open target help page")
def open_target_help(context):
    context.driver.get("https://help.target.com/help")


@when("target navigate to Help page")
def navigate_help_page(context):
    sleep(3)
    context.driver.find_element(By.XPATH, "//a[contains(@href, ‘/help’)]").click()


@then("target verify {number} UI elements exist")
def verify_ui(context, number):
    sleep(3)
    number = int(number)
    total = 0
    if context.driver.find_element(By.XPATH, "//*[contains(text(), 'Target Help')]"):
        total += 1
    if context.driver.find_element(By.ID, "j_id0:j_id2:j_id29:name"):
        total += 1
    if context.driver.find_element(By.CSS_SELECTOR, ".btn-sm.search-btn"):
        total += 1
    if context.driver.find_element(By.XPATH, "//*[text()='Browse all Help pages']"):
        total += 1
    grid_boxes = len(context.driver.find_elements(By.CSS_SELECTOR, "[class*='boxSmall txtAC']"))
    grid_contact = len(context.driver.find_elements(By.CSS_SELECTOR, ".grid_4.boxSmallr.txtAC"))
    grid_manage = len(context.driver.find_elements(By.CSS_SELECTOR, "[class*='salesforceBox']"))
    total += grid_manage + grid_boxes + grid_contact
    assert total == number, f"Error, expected {number} UI elements and got {total} UI elements"




