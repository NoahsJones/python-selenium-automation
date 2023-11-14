from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")


@when('TEACHER Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('TEACHER Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name, f'Expected {context.product_name}, but got {actual_name}'


@then('TEACHER Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    summary_text = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in summary_text, f"Expected '{amount} item' not in {summary_text}"



COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('TEACHER Open target product A-88062531 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-88062531')
    sleep(6)


@then('TEACHER Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]  # 'Color\nBlack' => ['Color', 'Black']
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@when('TEACHER Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, "#addToCartButtonOrTextIdFor85978614").click()  # find_element by default it will pick 1st one
    # all_buttons = context.driver.find_elements(*ADD_TO_CART_BTN)
    # all_buttons[2].click()


@when('TEACHER Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not shown in side navigation'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@then('TEACHER Verify search worked for {product}')
def verify_search(context, product):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    search_results_header = context.driver.find_element(*SEARCH_RESULT_TXT).text
    assert product in search_results_header, f'Expected text {product} not in {search_results_header}'
