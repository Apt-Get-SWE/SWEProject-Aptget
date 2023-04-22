from flask_restx import Resource, Namespace, fields
from flask import session, request
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

LINK = api.model('LinkUserAddress', {
    "aid": fields.String(description="aid to link to current user", required=True)
})

# link_user_address_field = api.model('LinkUserAddress', {
#     "aid", fields.String(description="AIDS of saved address"),
# })


class Users(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.produces(['application/json'])
    @api.response(200, 'User found successfully')
    @api.response(400, 'Not logged in!')
    def get(self) -> dict:
        """
        Returns the information of users that match the given UIDs.
        """

        # TODO Support queries with parameters other than UID
        uid = session.get('user_id')
        if uid is not None:
            # Get contact information from UID
            formatted_data = User.get_contact_info(uid)

            return {
                'Type': 'Data',
                'Title': 'User Contact Information',
                'Data': formatted_data
            }, 200

        return "Not logged in!", 400


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
            print(userInfo)
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


class LinkUserAddress(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @api.expect(LINK)
    @api.produces(['application/json'])
    def post(self):
        """
        Updates the aid field in user
        """
        if (uid := session.get('user_id')) is None:
            return {}, 401
        if (aid := request.json.get('aid')) is None:
            return {}, 400

        User.update_one(filters={'uid': uid}, new_values={"$set": {'aid': aid}})

        return {}, 200
