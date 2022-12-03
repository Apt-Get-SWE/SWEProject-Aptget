from flask_restful import Resource, request
from ..types.address import Address
from ..types.utils import parse_json


class Addresses(Resource):
    def get(self):
        data = parse_json(Address.find_all())

        # If zip code url param is provided, filter by zip code
        zipcode = request.args.get('zip')

        formatted_data = {}
        for addr in data:
            if zipcode and addr['zipcode'] != zipcode:
                continue
            formatted_data[addr['aid']] = addr

        return {
            'Type': 'Data',
            'Title': 'List of addresses',
            'Data': formatted_data
        }
