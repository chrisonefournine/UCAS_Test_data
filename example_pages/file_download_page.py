import httplib
from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage


class Download(BasePage):
    _example_a = {'by': By.CSS_SELECTOR, 'value': ('.example a:nth-of-type(1)')}
    #_example_a.__getattribute__('href')

    def __init__(self, driver):
        self.driver = driver
        self._visit("/download")

    def download_file(self):
        self._wait_for_is_displayed(self._example_a, 5)
        #download_link = self._example_a.get_attrubte('href')
        download_link = self.driver.find_element_by_css_selector('.example a:nth-of-type(1)').get_attribute('href')
        connection = httplib.HTTPConnection('the-internet.herokuapp.com')
        connection.request('HEAD', download_link)
        response = connection.getresponse()
        content_type = response.getheader('Content-type')
        content_length = response.getheader('Content-length')
        assert content_type == 'application/octet-stream'
        assert content_length > 0
