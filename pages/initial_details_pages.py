from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InitialDetailsPage(BasePage):
    _title = {"by": By.ID, "value": "titleCombo"}
    _gender = {"by": By.ID, "value": "genderCombo"}
    _first_name = {"by": By.ID, "value": "forenameText"}
    _family_name = {"by": By.ID, "value": "surnameText"}
    _day_of_birth = {"by": By.ID, "value": "dobDayCombo"}
    _month_of_birth = {"by": By.ID, "value": "dobMonthCombo"}
    _year_of_birth = {"by": By.ID, "value": "dobYearCombo"}
    _previous_button = {"by": By.ID, "value": "previous"}
    _next_button = {"by": By.CSS_SELECTOR, "value": "input:nth-child(4)"}
    _postal_message = {"by": By.XPATH, "value": "//div[@id='midBoxInternalWide']/p[@class='bold']"}

    def __init__(self, driver):
        self.driver = driver
        self.day = self._read_data(1, 1)
        self.month = self._read_data(1, 2)
        self.year = self._read_data(1, 3)
        self.title = self._read_data(1, 4)
        self.gender = self._read_data(1, 5)

    def details_(self):
        self._type(self._first_name, "Test")
        self._type(self._family_name, "Joe")
        self._select_dropdown(self._title, self.title)
        self._select_dropdown(self._gender, self.gender)
        self._select_dropdown(self._day_of_birth, self.day)
        self._select_dropdown(self._month_of_birth, self.month)
        self._select_dropdown(self._year_of_birth, self.year)
        self._click(self._next_button)
        self._wait_for_is_displayed(self._postal_message, 5)
        return self._is_displayed(self._postal_message)


