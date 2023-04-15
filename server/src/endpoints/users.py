from flask_restx import Resource, Namespace, fields
from flask import request, session
from ..types.user import User

api = Namespace("users", "Operations related to users")

POST_JSON = api.model('User', {
    "uid": fields.String(description="User ID", required=True),
    "email": fields.String(description="Email address of the user", required=True),
    "aid": fields.String(description="Address ID"),
    "fname": fields.String(description="First name of the user"),
    "lname": fields.String(description="Last name of the user"),
    "phone": fields.String(description="Phone number of the user"),
    "pfp": fields.String(description="Profile picture of the user"),
})

UID_JSON = api.model('UserID', {
    "uid": fields.String(description="User ID", required=True),
})

GET_RESPONSE = api.model('UserGetResponse', {
    "Type": fields.String(description="Type of response"),
    "Title": fields.String(description="Title of response"),
    "Data": fields.Raw(description="Data of response"),
})


class Users(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.produces(['application/json'])
    @api.response(200, 'User found successfully')
    def get(self) -> dict:
        """
        Returns the contact information of users that match the given UIDs.
        """

        # TODO Support queries with parameters other than UID
        uid = session.get('user_id')
        if uid is not None:
            # Get contact information from UID
            formatted_data = {}
            formatted_data[uid] = User.get_contact_info(uid)

            return {
                'Type': 'Data',
                'Title': 'User Contact Information',
                'Data': formatted_data
            }, 200

        return "No User ID provided!", 400
