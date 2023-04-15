import os
import pathlib
import requests
import google.auth.transport.requests
from flask import redirect, request, session
from flask_restx import Resource, Namespace
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from pip._vendor import cachecontrol
from ..types.user import User

api = Namespace("login", "Operations related to user login")

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # only for local testing

ENV = os.environ.get('ENV', 'local')  # default local, or else production
ROOT_URL = "http://localhost:8080" if ENV == 'local'\
    else "https://www.aptget.nyc"

GOOGLE_CLIENT_ID_TEST = "497541279341-qtudp4uvo0g39s0o4ops0mr2dsvemnp5.apps.googleusercontent.com"  # noqa
CLIENT_SECRET_FILE = os.path.join(pathlib.Path(
    __file__).parents[2], "CLIENT_CREDENTIALS_TEST.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=CLIENT_SECRET_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri=f"{ROOT_URL}/api/login/callback")


class GoogleLogIn(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.session = {'users': []}
        self.flow = flow
    """
    Calls google auth api to authenticate google user log in
    """

    def get(self):
        """
        Redirects user to google server for google account login authentication
        """
        if session.get("user_id") is not None:
            redirect(ROOT_URL)

        authorizationUrl, state = self.flow.authorization_url()
        if state:  # check
            session["state"] = state
            return redirect(authorizationUrl)
            # return {"Redirect URL": authorizationUrl, "state": state}
        else:
            # return {"Main menu" : f"{ROOT_URL}/"}
            return redirect(ROOT_URL)


class SaveUserLogin(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    def get(self):
        """
        Call back, grab user google_id and name. The google_idcan be used as our user_id.
        """  # noqa
        flow.fetch_token(authorization_response=request.url)
        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(
            session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID_TEST
        )

        google_id = id_info.get("sub")
        email = id_info.get("email")
        fname, lname = id_info.get("given_name"), id_info.get("family_name")
        pfp = id_info.get("picture")

        # check if user exists
        check = User.find_one({'uid': google_id})
        if check is None:
            # Insert user in DB if not already there
            user = User(google_id, email, fname=fname, lname=lname, pfp=pfp)
            user.save()

        session['user_id'] = google_id
        # messages = json.dumps

        return redirect(f"{ROOT_URL}/dashboard")


class RestrictedArea(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.ids = []

    def get(self):
        """
        Restricted area for logged in users.
        TODO: implement frontend page for logged in users
        """
        user_id = session.get("user_id")
        if user_id is not None:
            return {
                'Type': 'Data',
                'Data': {'Login Status': {'Login Status': f'Successfully logged in user {user_id}'}},
                'Status': 'Success'
            }
        else:
            return {
                'Type': 'Data',
                'Data': {'Login Status': {'Login Status': 'Not logged in!'}},
                'Status': 'Failed'
            }


class LogOut(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    def get(self):
        """
        Log out user
        """
        session.clear()
        return redirect(ROOT_URL)
