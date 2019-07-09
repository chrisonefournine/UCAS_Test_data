from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage

class Dropdown(BasePage):
    _dropdown = {"by": By.ID, "value": 'dropdown'}
    _title_ = {"by": By.CSS_SELECTOR, "value": "#content > div > h3"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/dropdown")
        assert self._is_displayed(self._title_)

    def click_dropdown(self, option_number):
        dropdown_element = self.driver.find_element(**self._dropdown)
        # assert dropdown_element[0].is_enabled() == True
        return self._select_dropdown(dropdown_element, option_number)


