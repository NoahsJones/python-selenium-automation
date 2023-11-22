from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def open_url(self, url):
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    
    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


    def wait_for_element_click(self, *locator):
        element = (self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable").click()
         )
        return element


    def wait_for_element_appear(self, *locator):
        (self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by {locator} not visible")
         )

    def wait_for_element_disappear(self, *locator):
        (self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"Element by {locator} is still visible")
         )

    def wait_for_url_change(self, initial_url):
        (self.wait.until(
            EC.url_changes(initial_url),
            message=f"URL {initial_url} did not change")
        )


    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, (f"Error, expected text '{expected_text}'"
                                              f"not in actual '{actual_text}'")


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, (f"Error, expected text '{expected_text}'"
                                              f"did not match actual '{actual_text}'")


    def verify_partial_url(self, expected_partial_url):
        # assert expected_partial_url in self.driver.current_url, \
        #     f'Expected {expected_partial_url} not in {self.driver.current_url}'
        self.wait.until(EC.url_contains(expected_partial_url), message=f"Expected '{expected_partial_url}' not in url")


    def get_current_window(self):
        return self.driver.current_window_handle


    def get_all_windows(self):
        return self.driver.window_handles


    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)


    def close_page(self):
        self.driver.close()


    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)





