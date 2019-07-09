import pytest
from example_pages import dropdown_page



class TestDropdown():

    @pytest.fixture
    def drop(self, driver):
        return dropdown_page.Dropdown(driver)

    def test_first_option(self, drop):
        assert drop.click_dropdown("Option 1")
