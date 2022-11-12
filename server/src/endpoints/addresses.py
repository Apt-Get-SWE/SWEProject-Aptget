from flask_restful import Resource
from ..types.address import Address
from ..types.utils import parse_json

class Addresses(Resource):
    def get(self):
        data = parse_json(Address.find_all())
        formatted_data = {}
        for addr in data:
            formatted_data[addr['aid']] = addr

        return {
            'Type' : 'Data',
            'Title' : 'List of addresses',
            'Data' : formatted_data
        }