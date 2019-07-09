import pytest
from example_pages import drag_drop_page



class TestDragDrop():

    @pytest.fixture
    def dragging(self, driver):
        return drag_drop_page.DragDropPage(driver)

    def test_dragdrop(self, dragging):
        assert dragging.drag_a_to_b() == "A"
