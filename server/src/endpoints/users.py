from flask_restx import Resource, Namespace, fields
from flask import session
from ..types.user import User
from ..types.address import Address

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


class GetUserAddress(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.produces(['application/json'])
    def get(self):
        """
        This is a developer only endpoint. It takes no paramter and uses user's uid stored inside
        the cookies session to retrieve address from database
        """
        user_id = session.get('user_id')
        if user_id is not None:
            userInfo = User.find_one(filters={'uid': user_id})
            user_aid = userInfo['aid']
            if user_aid is None:
                return {}, 200
            else:
                address = Address.find_one(filters={'aid': user_aid})
                if address is not None:
                    del address['_id']  # remove useless field
                return address, 200
        else:
            return "User must log in first", 401
