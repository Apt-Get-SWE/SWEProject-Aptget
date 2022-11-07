from flask_restful import Resource
from ..types.user import User
from ..types.utils import parse_json

class Users(Resource):
    def get(self):
        data = parse_json(User.find_all())
        return {
            'Type' : 'Data',
            'Title' : 'List of users',
            'Data' : data # TODO filter out sensitive data
        }