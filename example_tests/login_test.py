import pytest
from example_pages import login_pages



class TestLogin():

    @pytest.fixture
    def login(self, driver):
        return login_pages.LoginPage(driver)

    @pytest.mark.shallow
    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert(login.success_message_present())

    @pytest.mark.deep
    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "naughtybadpassword")
        assert login.failure_message_present() == True
        assert login.success_message_present() == False
