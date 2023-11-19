from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ACCOUNT_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    NAV_SIGN_IN = (By.XPATH, "//span[text()='Sign in' and @class='styles__ListItemText-sc-diphzn-1 jaMNVl']")


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




