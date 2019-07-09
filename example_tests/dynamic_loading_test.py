import pytest
from example_pages import dynamic_loading_page



@pytest.mark.deep
class TestDynamicLoading():

    @pytest.fixture
    def loading(self, driver):
        return dynamic_loading_page.DynamicLoadingPage(driver)

    def test_loading_1(self, loading):
        loading.load_example("1")
        assert loading.finish_text_present()

    def test_redered_element(self, loading):
        loading.load_example("2")
        assert loading.finish_text_present()