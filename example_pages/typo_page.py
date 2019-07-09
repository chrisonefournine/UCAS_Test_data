from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage

class TypoPage(BasePage):
    _typo_text = {"by": By.CSS_SELECTOR, "value": "div.example p:nth-of-type(2)"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/typos")

    def correct_text(self):
        return self._verify_text(self._typo_text)