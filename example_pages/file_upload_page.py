from selenium.webdriver.common.by import By
from example_pages.base_page import BasePage
import os


class FileUploadPage(BasePage):
    _file_upload = {"by": By.ID, "value": "file-upload"}
    _file_submit = {"by": By.ID, "value": "file-submit"}
    _uploaded_files = {"by": By.ID, "value": "uploaded-files"}

    def __init__(self, driver):
        self.driver = driver

    def upload_file(self):
        filename = 'some-file.rtf'
        print ('filename done')
        file = os.path.join(os.getcwd(), filename)
        self._visit("http://the-internet.herokuapp.com/upload")
        self._type(self._file_upload, file)
        print ('done typing')
        self._click(self._file_submit)
        print ('submitted')
        self._wait_for_is_displayed(self._uploaded_files, 10)
        print ('uploaded displayed')
        assert self._verify_text(self._uploaded_files) == filename, "uploaded file should be %s" % filename
        print ('text matches')

    def upload_success(self):
        return self._is_displayed(self._uploaded_files)