from pages.base_pagePOM import Page
from selenium.webdriver.common.by import By
from time import sleep


class CirclePage(Page):
    CIRCLE_TABS = (By.CSS_SELECTOR, "[data-test='about-tab']")
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    GOOGLE_PLAY_BUTTON = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")


    def open_circle_page(self):
        self.open_url("https://www.target.com/circle")


    def verify_can_click_tabs(self, *locator):
        tabs = self.find_elements(*self.TABS)
        current_url = ''
        for i in range(len(tabs)):
            self.find_elements(*self.TABS)[i].click()
            self.wait_for_url_change(current_url)
            current_url = self.driver.current_url


    def click_google_play(self):
        self.click(*self.GOOGLE_PLAY_BUTTON)
