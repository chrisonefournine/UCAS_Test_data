from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage

class Checkboxes(BasePage):
    _checkbox2 = {"by": By.CSS_SELECTOR, "value": '#checkboxes > input[type="checkbox"]:nth-child(3)'}
    _checkbox1 = {"by": By.CSS_SELECTOR, "value": '#checkboxes > input[type="checkbox"]:nth-child(1)'}
    _title_ = {"by": By.CSS_SELECTOR, "value": "#content > div > h3"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/checkboxes")
        assert self._is_displayed(self._title_)

    def is_checkbox1_selected(self):
        checkbox_element = self.driver.find_element(**self._checkbox1)
        return checkbox_element.is_selected()

    def is_checkbox2_selected(self):
        checkbox_element = self.driver.find_element(**self._checkbox2)
        return checkbox_element.is_selected()

    def select_checkbox(self, locator):
        self._click(locator)
