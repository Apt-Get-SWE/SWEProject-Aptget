from ...src.endpoints.menu import Menu
from ...src.constants import Constants

class TestMenu:
    def test_get(self):
        menu = Menu()
        assert menu.get() == Constants.Menu.TEST_MENU