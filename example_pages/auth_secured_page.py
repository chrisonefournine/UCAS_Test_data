from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage

class BasicAuth1(BasePage):
    _page_message = {"by": By.CSS_SELECTOR, "value": "div.example p"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("http://admin:admin@the-internet.herokuapp.com/basic_auth")

    def auth_success_message(self):
        self._wait_for_is_displayed(self._page_message, 2)
        assert self._verify_text(self._page_message) == 'Congratulations! You must have the proper credentials.'
        return self._is_displayed(self._page_message)