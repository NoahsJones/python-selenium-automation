from pages.base_pagePOM import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = By.XPATH, "//*[contains(text(), product_result)]"
    PRODUCTS = (By.CSS_SELECTOR, "[data-test*='ProductCardWrapper']")
    ADD_CART_BUTTONS = (By.CSS_SELECTOR, "button[ID*='addToCartButton']")
    SIDE_NAV_ADD_CART_BUTTON = (By.CSS_SELECTOR, "div[style='display: flex;'] [ID*='addToCartButton']")


    def verify_search_result(self, product):
        # sleep(4)  # Cannot find alternative for sleep
        # search_result_header = self.find_element(*self.SEARCH_RESULT_TEXT).text
        # assert product in search_result_header, f"Error, expected {product} and got this {search_result_header} instead"
        self.verify_partial_text(product, *self.SEARCH_RESULT_TEXT)

    def verify_search_url(self , expected_partial_url):
        # assert expected_keyword in self.driver.current_url, \
        #     f'Expected {expected_keyword} not in {self.driver.current_url}'
        self.verify_partial_url(expected_partial_url)


    def add_product_to_cart(self):
        self.find_elements(*self.ADD_CART_BUTTONS)[2].click()
        self.find_element(*self.SIDE_NAV_ADD_CART_BUTTON).click()

