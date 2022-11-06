import os
import pathlib
import requests
import google.auth.transport.requests
from flask import redirect, request, url_for
from flask_restx import Resource
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from pip._vendor import cachecontrol
from ..types.user import User


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #only for local testing

ENV = os.environ.get('ENV', 'local') # default local, or else production
ROOT_URL = "http://localhost:8000" if ENV == 'local' else "https://www.aptget.nyc"

GOOGLE_CLIENT_ID_TEST = "497541279341-qtudp4uvo0g39s0o4ops0mr2dsvemnp5.apps.googleusercontent.com"
CLIENT_SECRET_FILE = os.path.join(pathlib.Path(__file__).parents[2], "CLIENT_CREDENTIALS_TEST.json")
flow = Flow.from_client_secrets_file(
            client_secrets_file=CLIENT_SECRET_FILE,
            scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
            redirect_uri=f"{ROOT_URL}/callback")

class GoogleLogIn(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.session = {}
    """
    Calls google auth api to authenticate google user log in 
    """
    def get(self):
        """
        The url to jump to needs to be manually added to the google credentials. 
        #TODO: store state in sessions to track logged in users and parse user info to store to db. Verify if 
        """
        authorizationUrl, state = flow.authorization_url()
        if state: # check
            return redirect(authorizationUrl)
        else:
            return redirect(f"{ROOT_URL}/endpoints")

class VerifyUserLogin(Resource):
    
    def get(self):
        """
        Call back, grab user google_id and name. The google_id can be used as our user_id. 
        """
        flow.fetch_token(authorization_response=request.url)
        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID_TEST
        )

        google_id = id_info.get("sub")
        email = id_info.get("email")
        fname, lname = id_info.get("given_name"), id_info.get("family_name")
        pfp = id_info.get("picture")

        # Insert user in DB if not already there
        user = User(google_id, email, fname=fname, lname=lname, pfp=pfp)
        user.save()

        # TODO: redirect to register or load existing user data. 
        return user.to_dict()
    

class LogInSuccessPage(Resource):
    """
    Place holder for the page to jump to after log in is successful.
    """
    def get(self):
        # TODO: implement page
        return {
            'Type' : 'Data',
            'Data' : {'Login Status' : {'Login Status' : 'Successful'}},
            'Title' : 'Login Successful Page'
        }