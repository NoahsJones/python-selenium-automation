from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("Click on target circle")
def open_target_circle(context):
    context.driver.find_element(By.ID, "utilityNav-circle").click()
    sleep(5)


@then("Verify {number} benefit boxes display")
def benefit_boxes(context, number):
    benefit_box_list = context.driver.find_elements(By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
    assert len(benefit_box_list) == int(number), f'Error, there are {len(benefit_box_list)} elements instead of {number} elements for the benefit boxes'