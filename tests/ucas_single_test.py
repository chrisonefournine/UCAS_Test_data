import pytest
from pages import login_pages
from pages import initial_details_pages as idp
from pages import postal_address as pa
from pages import house_details as hd


class TestSingleApp():

    @pytest.fixture
    def register(self, driver):
        return login_pages.RegisterPage(driver)

    @pytest.fixture
    def first_det(self, driver):
        return idp.InitialDetailsPage(driver)

    @pytest.fixture
    def house_det(self, driver):
        return hd.HouseDetailsPage(driver)

    @pytest.fixture
    def post_det(self, driver):
        return pa.PostalAddressPage(driver)

    @pytest.mark.shallow
    def test_single_application(self, register, first_det, post_det, house_det):
        register.register_()
        first_det.details_()
        post_det.select_postal_()
        house_det.select_postal_()
        assert house_det.correct_text() == "LONDON"


