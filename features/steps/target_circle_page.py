from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
GOOGLE_PLAY_BUTTON = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")


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


@given("Open target circle page")
def open_circle_page(context):
    context.app.circle_page.open_circle_page()


@given("Store original window")
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()
    print('All windows:', context.windows)
    print('Current window:', context.original_window)


@when("Click Google Play button")
def click_google_play(context):
    #context.driver.find_element(*GOOGLE_PLAY_BUTTON).click()
    context.app.circle_page.click_google_play()


@when("Switch to new window")
def switch_window(context):
    # context.driver.wait.until(EC.new_window_is_opened)
    # new_window = context.driver.window_handles[1]
    # context.driver.switch_to.window(new_window)
    context.app.circle_page.switch_to_new_window()


@then("Verify Google Play Target page opened")
def verify_google_play_opened(context):
    # assert 'https://play.google.com/' in context.driver.current_url
    context.app.partner_page.verify_google_play_opened()

@then("Close current page")
def close(context):
    context.app.page.close_page()


@then("Return to original window")
def switch_to_original(context):
    # context.driver.switch_to.window(context.original_window)
    context.app.page.switch_to_window(context.original_window)

@then("Verify clicking through Circle tab works")
def verify_circle_tabs(context):
    context.app.circle_page.verify_can_click_tabs()