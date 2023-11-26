from pages.base_pagePOM import Page
from pages.main_pagePOM import MainPage
from pages.search_results_pagePOM import SearchResultsPage
from pages.cart_pagePOM import CartPage
from pages.circle_pagePOM import CirclePage
from pages.sign_in_pagePOM import SignInPage
from pages.partner_pagePOM import PartnerPage
from pages.help_pagePOM import HelpPage


class Application:

    def __init__(self, driver):
        self. search_results_page = SearchResultsPage(driver)
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.partner_page = PartnerPage(driver)
        self.help_page = HelpPage(driver)
