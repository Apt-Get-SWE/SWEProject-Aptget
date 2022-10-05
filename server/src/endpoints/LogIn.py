import os
import pathlib
from flask import redirect
from flask_restx import Resource
from google_auth_oauthlib.flow import Flow

GOOGLE_CLIENT_ID_TEST = "497541279341-qtudp4uvo0g39s0o4ops0mr2dsvemnp5.apps.googleusercontent.com"
CLIENT_SECRET_FILE = os.path.join(pathlib.Path(__file__).parents[2], "client_secret_test.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=CLIENT_SECRET_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/loggedin"
    )

class GoogleLogIn(Resource):
    """
    Calls google auth api to authenticate google user log in 
    """
    def get(self):
        """
        The url to jump to needs to be manually added to the google credentials. 
        #TODO: store state in sessions to track logged in users and parse user info to store to db. 
        """
        authorizationUrl, state = flow.authorization_url()
        return redirect(authorizationUrl)

class LogInSuccessPage(Resource):
    """
    Place holder for the page to jump to after log in is successful.
    """
    def get(self):
        return {"Login": "Successful"}