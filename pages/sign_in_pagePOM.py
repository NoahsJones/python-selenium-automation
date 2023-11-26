from pages.base_pagePOM import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN = (By.ID, "login")
    SIGN_IN_URL = 'https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin'
    TERMS_CONDITIONS = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")
    ACCOUNT_NOT_FOUND = (By.XPATH, "//*[contains(text(), 'your account')]")


    def verify_on_sign_in_page(self):
        self.verify_partial_url('signin')


    def log_in(self, email, password):
        self.input(email, *self.EMAIL_FIELD)
        self.input(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN)


    def open_sign_in_page(self):
        self.open_url(self.SIGN_IN_URL)


    def click_terms_conditions(self):
        self.click(*self.TERMS_CONDITIONS)


    def verify_terms_conditions_opened(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions')


    def verify_account_not_found(self):
        self.find_element(*self.ACCOUNT_NOT_FOUND)