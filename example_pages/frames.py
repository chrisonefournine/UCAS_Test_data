from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage


class SwitchFrames(BasePage):
    _editor = {"by": By.ID, "value": "tinymce"}
    _frame = {"by": By.ID, "value": "mce_0_ifr"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/tinymce")

    def switch_frame(self, text):
        frame = self.driver.find_element(**self._frame)
        self._switch_frame(frame)
        editor = self.driver.find_element(**self._editor)
        editor.clear()
        editor.send_keys(text)
        return self._verify_text(self._editor)