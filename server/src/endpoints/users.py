from flask_restful import Resource
from ..types.user import User
import json
from bson import json_util

def parse_json(data):
    return json.loads(json_util.dumps(data))

class Users(Resource):
    def get(self):
        raw = User.find_all()
        data = json.loads(json_util.dumps(raw))
        return {
            'Type' : 'Data',
            'Title' : 'List of users',
            'Data' : data # TODO filter out sensitive data
        }