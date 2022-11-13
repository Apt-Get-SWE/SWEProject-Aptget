"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restful import Api
import logging
from .src.endpoints.login import GoogleLogIn, LogInSuccessPage, VerifyUserLogin
from .src.constants import Constants
from .src.endpoints.index import Index
from .src.endpoints.menu import Menu
from .src.endpoints.posts import Posts
from .src.endpoints.addresses import Addresses

app = Flask(__name__, static_url_path='',
            static_folder=Constants.STATIC_FOLDER)
api = Api(app)
session = {}

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(asctime)s - '
                    '%(filename)s:%(lineno)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


api.add_resource(Index, "/")
api.add_resource(GoogleLogIn, "/login", resource_class_kwargs={})
api.add_resource(LogInSuccessPage, "/loggedin")
api.add_resource(VerifyUserLogin, "/callback")
api.add_resource(Menu, "/main_menu")
api.add_resource(Posts, "/posts")
api.add_resource(Addresses, "/addr")

if __name__ == "__main__":
    app.run(debug=True)
