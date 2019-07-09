import pytest
from example_pages import frames



class TestSwitchFrame():

    @pytest.fixture
    def main_frame(self, driver):
        return frames.SwitchFrames(driver)

    def test_switch_text(self, main_frame):
        assert main_frame.switch_frame('Bum tish')