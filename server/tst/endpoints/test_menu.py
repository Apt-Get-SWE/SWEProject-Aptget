import pytest
from ...src.endpoints.menu import Menu
from ...src.constants import Constants

class TestMenu:
    @pytest.fixture
    def get_test_menu(self):
        return Constants.Menu.TEST_MENU

    def test_get(self, get_test_menu):
        menu = Menu()
        assert menu.get() == get_test_menu