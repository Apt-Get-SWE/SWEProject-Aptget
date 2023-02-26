from flask_restx import Resource, Namespace, fields
from flask import request
from ..map.map_utils import serializeParameters

api = Namespace("serialize", "Serializing google api request data")

dummyQueryModel = api.model("queryRequest", {
    'Request Type': fields.String,
    'Validate': fields.Boolean,
    'URL': fields.String,
})


class GoogleAPIRequest(Resource):
    @api.expect(dummyQueryModel)
    def post(self):
        """
        Serialize google api request parameters. Removes invalid field. Will always return a dictionary object. This is meant for internal use for developers to help implement other backend functions and endpoints.
        """
        data = request.get_json()
        serializedData = serializeParameters(data)
        return serializedData
