from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = By.XPATH, "//*[contains(text(), product_result)]"


    def verify_search_result(self, product):
        sleep(4)  # Cannot find alternative for sleep
        search_result_header = self.find_element(*self.SEARCH_RESULT_TEXT).text
        assert product in search_result_header, f"Error, expected {product} and got this {search_result_header} instead"


    def verify_search_url(self ,expected_keyword):
        assert expected_keyword in self.driver.current_url, \
            f'Expected {expected_keyword} not in {self.driver.current_url}'