from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
@when("Click on target circle")
def open_target_circle(context):
    context.driver.find_element(By.ID, "utilityNav-circle").click()


@then("Verify {number} benefit boxes display")
def benefit_boxes(context, number):
    context.driver.wait.until(
        EC.visibility_of_element_located(BENEFIT_BOXES)
    )
    benefit_box_list = context.driver.find_elements(By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
    assert len(benefit_box_list) == int(number), f'Error, there are {len(benefit_box_list)} elements instead of {number} elements for the benefit boxes'