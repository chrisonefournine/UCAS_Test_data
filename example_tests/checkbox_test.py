import pytest
from example_pages import checkboxes_page



class TestCheckboxes():

    @pytest.fixture
    def check(self, driver):
        return checkboxes_page.Checkboxes(driver)

    def test_page_land_checkbox(self, check):
        assert check.is_checkbox1_selected() == False
        assert check.is_checkbox2_selected() == True

    def test_page_select_checkbox(self, check):
        check.select_checkbox(check._checkbox1)
        assert check.is_checkbox1_selected() == True
        assert check.is_checkbox2_selected() == True

