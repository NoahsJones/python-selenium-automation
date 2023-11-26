from pages.base_pagePOM import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


class MainPage(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ACCOUNT_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    NAV_SIGN_IN = (By.XPATH, "//span[text()='Sign in' and @class='styles__ListItemText-sc-diphzn-1 jaMNVl']")
    SIGN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")


    def open_main(self):
        self.open_url("https://www.target.com/")


    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)


    def open_cart(self):
        # self.find_element(*self.CART_ICON).click()
        # self.wait(*self.CART_ICON)
        self.wait_for_element_click(*self.CART_ICON)
        # sleep(0.2)


    def open_account_side_nav(self, *locator):
        self.find_element(*self.ACCOUNT_SIDE_NAV).click()


    def open_signin(self, *locator):
        self.find_element(*self.NAV_SIGN_IN).click()


    def verify_user_logged_in(self):
        self.wait_for_url_change('https://www.target.com/login')


    def hover_over_signin(self):
        signin_btn = self.find_element(*self.SIGN_IN)
        actions = ActionChains(self.driver)
        actions.move_to_element(signin_btn)
        actions.perform()
        sleep(4)


    def verify_signin_arrow_shown(self):
        self.wait_for_element_visible(*self.SIGN_IN_ARROW)




