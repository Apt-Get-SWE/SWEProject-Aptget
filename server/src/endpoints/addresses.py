from flask_restx import Resource, Namespace, fields
from flask import request
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

GET_RESPONSE = api.model('AddressGetResponse', {
    "Type": fields.String(description="Type of response"),
    "Title": fields.String(description="Title of response"),
    "Data": fields.Raw(description="Data of response"),
})


class Addresses(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.produces(['application/json'])
    @api.marshal_with(GET_RESPONSE)
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

        # Parse aid, building, city, state, zipcode from json
        addr = Address.from_json(json)
        try:
            addr.save()
            return "Address created successfully", 201
        except Exception as e:
            return f'Error saving post: {e}', 500
