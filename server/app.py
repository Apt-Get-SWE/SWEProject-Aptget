"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, send_from_directory
from flask_restful import Api, Resource
import logging
from .src.endpoints.endpoints import Endpoints
from .src.endpoints.login import GoogleLogIn, LogInSuccessPage, VerifyUserLogin

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)
session = {}

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Index(Resource):
    def get(self):
        return send_from_directory(app.static_folder, 'index.html')


api.add_resource(Index, "/")
api.add_resource(Endpoints, "/endpoints")
api.add_resource(GoogleLogIn, "/login", resource_class_kwargs={})
api.add_resource(LogInSuccessPage, "/loggedin")
api.add_resource(VerifyUserLogin, "/callback")

if __name__ == "__main__":
    app.run(debug=True)
