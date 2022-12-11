from flask_restx import Resource
from flask import request
from ..types.address import Address
from ..types.utils import parse_json


class Addresses(Resource):
    def get(self):
        '''
        Returns a list of all existing addresses
        '''
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

    def post(self):
        '''
        Add a new address
        '''
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        # Parse aid, building, city, state, zipcode from json
        addr = Address.from_json(json)
        try:
            addr.save()
            return "Address created successfully", 201
        except Exception as e:
            return f'Error saving post: {e}', 500
