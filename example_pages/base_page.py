from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select as WebDriverSelect
from example_tests import config

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
         if url.startswith("http"):
             self.driver.get(url)
         else:
             self.driver.get(config.baseurl + url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed()
        except NoSuchElementException:
                return False
        return True

    def _wait_for_is_displayed(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True

    def _verify_css_value(self, locator, property_name):
        return self._find(locator).value_of_css_property(property_name)

    def _verify_text(self, locator):
        return self._find(locator).text

    def _drag_element(self, element, target):
        drag_drop = ActionChains(self.driver)
        drag_drop.click_and_hold(element).move_by_offset(-1, -1).move_to_element(target).release().perform()

    def _select_dropdown(self, locator, option_number):
        select_list = WebDriverSelect(locator)
        select_list.select_by_visible_text(option_number)
        selected_option = select_list.first_selected_option.text
        return selected_option == (option_number), ("Selected option should be " + (option_number))

    def _switch_frame(self, locator):
        self.driver.switch_to_frame(locator)

    def _is_enabled(self, locator):
        return self._find(locator).is_enabled






