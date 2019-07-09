from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    _login_button = {"by": By.NAME, "value": "btnLogin"}
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _register_button = {"by": By.NAME, "value": "btnRegister"}
    _register_next = {"by": By.CSS_SELECTOR, "value": "input:nth-child(4)"}
    _register_message = {"by": By.CSS_SELECTOR, "value": "#strapLineApply > h1"}
    _t_c = {"by": By.ID, "value": "termsCheckBox"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("appreg/SecurityServlet")
        assert self._wait_for_is_displayed(self._login_button, 5)

    def register_(self):
        self._click(self._register_button)
        self._wait_for_is_displayed(self._register_next, 10)
        self._click(self._register_next)
        self._wait_for_is_displayed(self._t_c, 10)
        self._click(self._t_c)
        self._click(self._register_next)

