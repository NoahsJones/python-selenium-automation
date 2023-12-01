from pages.base_pagePOM import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
from support.logger import logger


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER_TITLE = (By.CSS_SELECTOR, "h1")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    RETURNS_EXCHANGES = (By.XPATH, "//a[contains(text(), 'Returns & Exchanges')]")
    RETURNS = (By.CSS_SELECTOR, "[title='Returns']")
    def open_help_returns(self):
        self.open_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")
        #self.driver.execute_script("window.scrollBy(0,500)", "")
       # self.click(*self.RETURNS_EXCHANGES)
       # self.click(*self.RETURNS)


    def verify_returns_opened(self):
        self.wait_for_element_appear(*self.HEADER_RETURNS)


    def select_topic(self, topic):
        topic_selection = self.find_element(*self.TOPIC_SELECTION)
        logger.info(f'Selecting {topic} from dropdown')
        select = Select(topic_selection)
        select.select_by_value(topic)


    def verify_topic_opened(self):
        # self.wait_for_element_appear(*self.HEADER_PROMOTIONS)
        self.wait_for_element_appear(*self.HEADER_TITLE)
