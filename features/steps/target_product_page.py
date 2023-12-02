from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

PRODUCT_COLORS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
PRODUCT_FOLGERS_COFFEE = (By.CSS_SELECTOR, "[alt='Folgers Classic Medium Roast Ground Coffee']")
FOLGERS_COFFEE_SIDE_NAV = (By.ID, "addToCartButtonOrTextIdFor13397813")
VIEW_CART = (By.CSS_SELECTOR, "[href='/cart']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")

@given("Open product page")
def open_product_flannel(context):
    context.driver.get('https://www.target.com/p/men-39-s-midweight-flannel-long-sleeve-button-down-shirt-goodfellow-38-co-8482/-/A-88552425?preselect=88257254#lnk=sametab')
    sleep(6)

@when("target add {product} to cart")
def add_product(context, product):
    # sleep(0.2)
    # context.driver.find_element(*PRODUCT_FOLGERS_COFFEE).click()
    # sleep(0.2)
    # context.driver.wait.until(EC.visibility_of_element_located(FOLGERS_COFFEE_SIDE_NAV)) #Wait until product is open and elements appear
    # context.driver.find_element(*FOLGERS_COFFEE_SIDE_NAV).click()
    #
    # context.driver.wait.until(EC.element_to_be_clickable(VIEW_CART))
    # context.driver.find_element(*VIEW_CART).click()
    context.app.search_results_page.add_product_to_cart()


@then('Verify search worked for {product}')
def verify_search(context, product):
    sleep(0.2)
    context.driver.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-test='resultsHeading']"), product))
    expected_result = product
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert expected_result in actual_result, f"Error, expected {expected_result} is not in actual '{actual_result}'"
    #sleep(2)



@then('Verify {product} in search result url')#This is the And in the feature file
def verify_search_url(context, product):
    # sleep(0.2)
    # context.driver.wait.until(EC.url_contains(product))
    # assert product in context.driver.current_url
    context.app.search_results_page.verify_search_url(product)



@then("target verify {product_result} is found")
def verify_product_search(context, product_result):
    # sleep(4)  #Cannot find alternative for sleep
    # expected_result = product_result
    # actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), product_result)]").text
    # assert expected_result in actual_result, f"Error, expected {expected_result} and got this {actual_result} instead"
    context.app.search_results_page.verify_search_result(product_result)


@then('Verify product colors')
def verify_product_colors(context):
    colors = context.driver.find_elements(*PRODUCT_COLORS)
    actual_colors = []
    expected_colors = ['Black', 'Cream', 'Gray', 'Red', 'Orange', 'Burgundy', 'Navy Blue', 'Light Navy Blue', 'Olive Green']
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(selected_color)
        sleep(2)  #used for slowing down the testing to see it work. Works fine without sleep since elements are already loaded.
    assert expected_colors == actual_colors, f"Error, {expected_colors} is not the same as {actual_colors}"


@then("target verify product title and image")
def verify_products_name_img(context):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.page.scroll_down(4000)

    all_products = context.driver.find_elements(*LISTINGS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
        sleep(0.2)

