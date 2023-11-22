from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.sign_in_page import SignInPage
from pages.partner_page import PartnerPage


class Application:

    def __init__(self, driver):
        self. search_results_page = SearchResultsPage(driver)
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.partner_page = PartnerPage(driver)
