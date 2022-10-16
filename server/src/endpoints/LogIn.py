import os
import pathlib
import requests
import google.auth.transport.requests
from flask import redirect, request, url_for
from flask_restx import Resource
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from pip._vendor import cachecontrol

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #only for local testing

GOOGLE_CLIENT_ID_TEST = "497541279341-qtudp4uvo0g39s0o4ops0mr2dsvemnp5.apps.googleusercontent.com"
CLIENT_SECRET_FILE = os.path.join(pathlib.Path(__file__).parents[2], "CLIENT_CREDENTIALS_TEST.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=CLIENT_SECRET_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:8000/callback"
    )

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
            return redirect("http://127.0.0.1:8000/endpoints")

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
        name = id_info.get("name")

        # TODO: redirect to register or load existing user data. 
        return {google_id:name}
    

class LogInSuccessPage(Resource):
    """
    Place holder for the page to jump to after log in is successful.
    """
    def get(self):
        print(request.args["user"])
        return {"Login": "Successful"}