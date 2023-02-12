from flask_restx import Resource
from ..constants import Constants


class Menu(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    def get(self):
        '''
        Returns the formatted menu
        '''
        return Constants.Menu.TEST_MENU
