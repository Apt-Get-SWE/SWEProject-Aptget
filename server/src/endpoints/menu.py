from flask_restx import Resource
from ..constants import Constants


class Menu(Resource):
    def get(self):
        '''
        Returns the formatted menu
        '''
        return Constants.Menu.TEST_MENU
