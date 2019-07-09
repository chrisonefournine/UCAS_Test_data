import pytest
from example_pages import auth_secured_page

class TestBasicAuth():

    @pytest.fixture
    def auth(self, driver):
        return auth_secured_page.BasicAuth1(driver)

    def test_auth_success_message(self, auth):
        assert auth.auth_success_message() == True