from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HouseDetailsPage(BasePage):
    _house_no = {"by": By.ID, "value": "houseNoText"}
    _post_code = {"by": By.ID, "value": "postcodeText"}
    _city = {"by": By.ID, "value": "addrLine4Text"}
    _previous_button = {"by": By.ID, "value": "previous"}
    _next_button = {"by": By.CSS_SELECTOR, "value": "input:nth-child(4)"}

    def __init__(self, driver):
        self.driver = driver

    def select_postal_(self):
        self._type(self._house_no, "10")
        self._type(self._post_code, "SW1A 2AA")
        self._click(self._next_button)
        self._wait_for_is_displayed(self._city, 5)

    def correct_text(self):
        return self._verify_text(self._city)


