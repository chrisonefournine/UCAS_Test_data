from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage

class BrokenImagePage (BasePage):
    _broken_image =  {"by": By.XPATH, "value": "//img[1]"}
    _placeholder_image = {"by": By.XPATH, "value": "//img[3]"}
    _title = {"by" : By.XPATH, "value": "//div[@class='example']/h3"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/broken_images")
        assert self._is_displayed(self._title)

    def image_present (self):
        return self._is_displayed(self._broken_image)

    def image_thumb (self):
        return self._wait_for_is_displayed(self._placeholder_image, 5)

    def image_height (self):
        return self._verify_css_value(self._placeholder_image, 'height')

    def image_width (self):
        return self._verify_css_value(self._placeholder_image, 'width')

