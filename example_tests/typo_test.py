import pytest
from example_pages import typo_page



class TestTypo():

    @pytest.fixture
    def typo(self, driver):
        return typo_page.TypoPage(driver)

    def test_valid_text(self, typo):
        assert typo.correct_text() == "Sometimes you'll see a typo, other times you won't."
