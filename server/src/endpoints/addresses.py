import logging
from flask_restx import Resource, Namespace, fields
from flask import request, session
from ..types.address import Address
from ..types.utils import parse_json

api = Namespace("addresses", "Operations related to addresses")


addresses_field = api.model('Address', {
    "aid": fields.String(description="Address ID", required=True),
    "building": fields.String(description="Address building name"),
    "city": fields.String(description="Address city name"),
    "state": fields.String(description="Address state name"),
    "zipcode": fields.String(description="Address zip code"),
})

aid_field = api.model('Address ID', {
    "aid": fields.String(description="Address ID", required=True)
})

GET_RESPONSE = api.model('AddressGetResponse', {
    "Type": fields.String(description="Type of response"),
    "Title": fields.String(description="Title of response"),
    "Data": fields.Raw(description="Data of response"),
})


class Addresses(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.doc(params={'addressPrefix': 'Address prefix'})
    @api.produces(['application/json'])
    @api.marshal_with(GET_RESPONSE)
    def get(self):
        '''
        Returns a list of all existing addresses
        '''
        prefix = request.args.get('addressPrefix')
        logging.info(f'addressPrefix: {prefix}')

        if prefix:
            filters = {
                'building': {
                    '$regex': f'^{prefix}'
                }
            }
            data = parse_json(Address.find_all(filters))
            logging.info(f'Found {len(data)} addresses')
        else:
            data = parse_json(Address.find_all())
            logging.info(f'No prefix Found {len(data)} addresses')

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

    @api.expect(addresses_field)
    @api.response(201, 'Address created successfully')
    @api.response(500, 'Error saving address')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def post(self):
        '''
        Add a new address
        '''
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        cookie_user_id = session.get("user_id")

        if cookie_user_id is None:
            return "User not logged in", 401

        # Parse aid, building, city, state, zipcode from json
        addr = Address.from_json(json)
        try:
            addr.save()
            return "Address created successfully", 201
        except Exception as e:
            return f'Error saving address: {e}', 500

    @api.expect(addresses_field)
    @api.response(200, 'Address updated successfully')
    @api.response(500, 'Error saving address')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def put(self):
        '''
        Modify an existing address
        '''
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        cookie_user_id = session.get("user_id")

        if cookie_user_id is None:
            return "User not logged in", 401

        # Parse aid, building, city, state, zipcode from json
        try:
            addr = Address.from_json(json)
            addr.save()
            return "Address modified successfully", 200
        except Exception as e:
            return f'Error saving address: {e}', 500

    @api.expect(aid_field)
    @api.response(200, 'Address deleted successfully')
    @api.response(500, 'Error deleting address')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def delete(self):
        """
        Deletes an address
        """
        # For deleting an existing address
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
        else:
            return 'Content-Type not supported!', 415

        # TODO: Needs more access control here. Only admins should be able to delete addresses
        cookie_user_id = session.get("user_id")

        if cookie_user_id is None:
            return "User not logged in", 401

        try:
            Address.delete_one({'aid': json['aid']})
            return "Address deleted successfully", 200
        except Exception as e:
            return f'Error deleting address: {e}', 500
