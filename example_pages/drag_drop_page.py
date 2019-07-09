from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage
import time


class DragDropPage(BasePage):
    _column_a = {"by": By.CSS_SELECTOR, "value": "#column-a"}
    _column_b = {"by": By.CSS_SELECTOR, "value": "#column-b"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/drag_and_drop")
        assert self._is_displayed(self._column_a)
        assert self._is_displayed(self._column_b)

    def drag_a_to_b(self):
        a = self.driver.find_element(**self._column_a)
        b = self.driver.find_element(**self._column_b)
        self._drag_element(a, b)
        time.sleep(1)
        return self._verify_text(self._column_b)

    def drag_b_to_a(self):
        a = self.driver.find_element(**self._column_a)
        b = self.driver.find_element(**self._column_b)
        self._drag_element(b, a)
        time.sleep(1)
        return self._verify_text(self._column_b)