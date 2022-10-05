"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
import os
import pathlib
from flask import Flask, send_from_directory, redirect, request
from flask_restful import Api
# from .src.endpoints.endpoints import Endpoints
from google_auth_oauthlib.flow import Flow

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)

GOOGLE_CLIENT_ID_TEST = "497541279341-qtudp4uvo0g39s0o4ops0mr2dsvemnp5.apps.googleusercontent.com"
CLIENT_SECRET_FILE = os.path.join(pathlib.Path(__file__).parent, "client_secret_test.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=CLIENT_SECRET_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/loggedin"
    )


@app.route("/", defaults={'path': ''})
def serve(path = ''):
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/login")
def login():
    authorizationUrl, state = flow.authorization_url()
    return redirect(authorizationUrl)

@app.route("/loggedin")
def loggedin():
    # flow.fetch_token(authorization_response=request.url)
    return "Log in successful!"

# api.add_resource(Endpoints, "/endpoints")

if __name__ == "__main__":
    app.run(debug=True)
