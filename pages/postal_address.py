from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PostalAddressPage(BasePage):
    _uk_input = {"by": By.ID, "value": "locationRadioHome"}
    _non_uk_input = {"by": By.ID, "value": "locationRadioOverseas"}
    _bf_input = {"by": By.ID, "value": "locationRadioBFPO"}
    _previous_button = {"by": By.ID, "value": "previous"}
    _next_button = {"by": By.CSS_SELECTOR, "value": "input:nth-child(4)"}
    _postal_message = {"by": By.XPATH, "value": "//*[@id='midBoxInternalWide']/p/text()"}
    _house_msg = {"by": By.XPATH, "value": "//*[@id='midBoxInternalWide']/p[1]"}

    def __init__(self, driver):
        self.driver = driver

    def select_postal_(self):
        self._click(self._uk_input)
        self._click(self._next_button)
        self._wait_for_is_displayed(self._house_msg, 5)
        return self._is_displayed(self._house_msg)

