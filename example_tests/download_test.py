import pytest
import os
import self as self
import tempfile
from example_pages import file_download_page

class TestDownload():

    @pytest.fixture
    def download (self, driver):
        return file_download_page.Download(driver)

    def test_download_1 (self, download):
        download.download_file()

