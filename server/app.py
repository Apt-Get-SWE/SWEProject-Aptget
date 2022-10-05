"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, send_from_directory
from flask_restful import Api
from .src.endpoints.endpoints import Endpoints

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


api.add_resource(Endpoints, "/endpoints")
