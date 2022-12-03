from flask_restful import Resource
from ..constants import Constants


class Menu(Resource):
    def get(self):
        return Constants.Menu.TEST_MENU
