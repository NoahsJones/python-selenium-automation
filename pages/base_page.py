class Page:
    def __init__(self, driver):
        self.driver = driver


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def open_url(self, url):
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    
    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)