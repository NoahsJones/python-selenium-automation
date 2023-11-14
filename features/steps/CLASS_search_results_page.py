from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
CART_SUMMARY = (By.CSS_SELECTOR, ".styles__CartSummarySpan-sc-odscpb-3.jaXVgU")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[class*='StyledHeading'][data-test='product-title']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyleHeading']")
SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

@given("Open target product A-88062531 page")
def open_target(context):
    context.driver.get("https://www.target.com/p/women-s-crewneck-cotton-pullover-sweater-universal-thread/-/A-88062531?preselect=87817585#lnk=sametab")
    sleep(6)


@then("Verify user can click through colors")
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        #print(selected_color)
        actual_colors.append(selected_color)

    #print(actual_colors)
    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match Actual {actual_colors}'


@when("Click on Add to Cart button")
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click() #find_element by default will click on the first element it finds
    #all_buttons = context.driver.find_elements(*ADD_TO_CART_BTN)
    #all_buttons[0].click()
    sleep(6)


@then("Verify cart has {amount} item(s)")
def verify_cart_items(context, amount):
    summary_text = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in summary_text, f"Expected '{amount} item' not in {summary_text}"


@then("Verify cart has correct product")
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name, f"Expected {context.product_name}, but got {actual_name}"


@when("Store product name")
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message="product name not shown in side navigation"
        )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when("Open cart page")
def open_cart_page(context):
    context.driver.get("https://www.target.com/cart")

