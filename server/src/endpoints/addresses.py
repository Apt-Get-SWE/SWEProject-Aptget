import logging
from flask_restx import Resource, Namespace, fields
from flask import request, session, url_for
from ..types.address import Address
from ..types.user import User
from ..types.utils import parse_json

api = Namespace("addresses", "Operations related to addresses")


addresses_field = api.model('Address', {
    "building": fields.String(description="Address building name"),
    "city": fields.String(description="Address city name"),
    "state": fields.String(description="Address state name"),
    "zipcode": fields.String(description="Address zip code"),
})

GET_RESPONSE = api.model('AddressGetResponse', {
    "Type": fields.String(description="Type of response"),
    "Title": fields.String(description="Title of response"),
    "Data": fields.Raw(description="Data of response"),
    "links": fields.Raw(description="Links for HATEOAS"),
})


class Addresses(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.doc(params={'addressPrefix': 'Address prefix'})
    @api.produces(['application/json'])
    @api.marshal_with(GET_RESPONSE)
    def get(self):
        """
        Returns a list of all existing addresses, or a list of addresses that match the address prefix.
        If a `zip` parameter is provided, the addresses will be filtered by zip code.

        Returns:
            A dictionary with the following keys:
                - 'Type': A string indicating the type of data returned.
                - 'Title': A string indicating the title of the data returned.
                - 'Data': A dictionary containing the formatted address data.
                - 'links': A dictionary containing links for creating, updating, and deleting addresses.
        """
        prefix = request.args.get('addressPrefix')
        logging.info(f'addressPrefix: {prefix}')

        filters = {'building': {'$regex': f'^{prefix}'}} if prefix else {}
        data = parse_json(Address.find_all(filters))
        logging.info(f'{"No" if not prefix else ""} prefix Found {len(data)} addresses')

        zipcode = request.args.get('zip')
        formatted_data = {}

        for addr in data:
            if zipcode and addr['zipcode'] != zipcode:
                continue

            url = url_for('api.addresses_addresses', _external=True)
            addr["links"] = {
                "self": f"{url}?aid={addr['aid']}",
                "update": {"url": f"{url}?aid={addr['aid']}", "aid": addr['aid']},
                "delete": {"url": f"{url}?aid={addr['aid']}", "aid": addr['aid']}
            }
            formatted_data[addr['aid']] = addr

        return {
            'Type': 'Data',
            'Title': 'List of addresses',
            'Data': formatted_data,
            'links': {
                'create_address': {
                    "url": url_for('api.addresses_addresses', _external=True, _method='POST'),
                    "fields": {
                        "aid": "Address ID (required)",
                        "building": "Address building name",
                        "city": "Address city name",
                        "state": "Address state name",
                        "zipcode": "Address zip code"
                    }
                }
            }
        }

    @api.expect(addresses_field)
    @api.response(201, 'Address created successfully')
    @api.response(500, 'Error saving address')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def post(self):
        """Add a new address.

        Parses JSON data from the request and creates a new Address object from it.
        The Address object is then saved to the database. If the save is successful,
        the function returns a response with a HTTP status code of 201. If there is an
        error, the function returns an error message and a HTTP status code of 500.

        Returns:
            A tuple containing a response message and a HTTP status code.
        """
        json_data = request.get_json(force=True)
        user_id = session.get('user_id')
        if not user_id:
            return 'User not logged in', 401
        try:
            addr = Address.from_json(json_data)
            response = addr.save()
            return response, 201
        except Exception as e:
            return f'Error saving address: {e}', 500

    @api.expect(addresses_field)
    @api.response(200, 'Address updated successfully')
    @api.response(500, 'Error saving address')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def put(self):
        """Modify an existing address.

        Parses JSON data from the request and updates the corresponding Address object in the database.
        If the update is successful, the function returns a response with a HTTP status code of 200.
        If there is an error, the function returns an error message and a HTTP status code of 500.

        Returns:
            A tuple containing a response message and a HTTP status code.
        """
        json_data = request.get_json(force=True)
        user_id = session.get('user_id')
        if not user_id:
            return 'User not logged in', 401
        try:
            Address.from_json(json_data).save()
            return 'Address modified successfully', 200
        except Exception as e:
            return f'Error modifying address: {e}', 500

    @api.doc(params={'aid': 'The Address ID'})
    @api.response(200, 'Address deleted successfully')
    @api.response(500, 'Error deleting address')
    @api.response(415, 'Content-Type not supported!')
    @api.produces(['text/plain'])
    def delete(self):
        """Deletes an address.

        Deletes the corresponding Address object in the database based on the provided aid.
        If the delete is successful, the function returns a response with a HTTP status code of 200.
        If the address does not exist or there is an error during deletion, the function returns
        an error message and a HTTP status code of 400 or 500 respectively.

        Returns:
            A tuple containing a response message and a HTTP status code.
        """
        aid = request.args.get('aid')
        if not aid:
            return 'aid not provided', 400
        if not Address.exists({'aid': aid}):
            return 'Address does not exist', 400
        user_id = session.get('user_id')
        if not user_id:
            return 'User not logged in', 401
        user_obj = User.find_one(filters={'uid': user_id})
        if not user_obj or user_obj['role'] != 'admin':
            return 'User not admin', 401
        try:
            Address.delete_one({'aid': aid})
            return 'Address deleted successfully', 200
        except Exception as e:
            return f'Error deleting address: {e}', 500
