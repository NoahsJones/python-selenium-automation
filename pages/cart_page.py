from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Cart(Page):
    EMPTY_CART = (By.XPATH, "//h1[text()='Your cart is empty']")
    def verify_cart_empty(self):
        expected_result = 'cart is empty'
        actual_result = self.find_element(*self.EMPTY_CART).text
        assert expected_result in actual_result, f"Expected {expected_result} but got {actual_result}"
