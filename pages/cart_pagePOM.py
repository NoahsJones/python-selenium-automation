from pages.base_pagePOM import Page
from selenium.webdriver.common.by import By
from time import sleep

class CartPage(Page):
    # EMPTY_CART = (By.XPATH, "//h1[text()='Your cart is empty']")
    HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_PRODUCT = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        # expected_result = 'cart is empty'
        # actual_result = self.find_element(*self.HEADER).text
        # assert expected_result in actual_result, f"Expected {expected_result} but got {actual_result}"
        self.verify_text('Your cart is empty', *self.HEADER)


    def open_cart_page(self):
        self.open_url("https://www.target.com/cart")


    def verify_product_in_cart(self, product):
        self.verify_partial_text(product, *self.CART_PRODUCT)
