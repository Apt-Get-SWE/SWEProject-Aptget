from flask_restx import Resource, Namespace, fields
from flask import request
from ..map.map_utils import serializeParameters

api = Namespace("serialize", "Serializing google api request data", path="/api/serialize")

dummyQueryModel = api.model("queryRequest", {
    'Request Type': fields.String,
    'Validate': fields.Boolean,
    'URL': fields.String,
})


class GoogleAPIRequest(Resource):
    @api.expect(dummyQueryModel)
    def post(self):
        """
        Serialize google api request parameters. Removes invalid field. Will always return a dictionary object.
        """
        data = request.get_json()
        serializedData = serializeParameters(data)
        return serializedData
