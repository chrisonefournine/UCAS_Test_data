import pytest
from example_pages import image_pages



class TestBrokenImages():

    @pytest.fixture
    def images(self, driver):
        return image_pages.BrokenImagePage(driver)

    def test_image_not_rendered(self, images):
        # Need to integrate with Browser mob to check status code response.
        assert images.image_present() == True

    def test_image_thumbnail(self, images):
        assert images.image_thumb()

    def test_image_css(self, images):
        assert images.image_height() == '90px'
        assert images.image_width() == '120px'