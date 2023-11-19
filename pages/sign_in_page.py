from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN = (By.ID, "login")
    def verify_on_sign_in_page(self):
        self.verify_partial_url('signin')


    def log_in(self, email, password):
        self.input(email, *self.EMAIL_FIELD)
        self.input(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN)
