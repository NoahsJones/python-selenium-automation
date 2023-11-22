from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class PartnerPage(Page):


    #Android Google Play:
    def verify_google_play_opened(self):
        self.verify_partial_url('https://play.google.com/')


    #iOS store:
