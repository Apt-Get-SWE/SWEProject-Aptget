"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Api
import logging
from .src.endpoints.login import GoogleLogIn, LogInSuccessPage, api as login
from .src.constants import Constants
from .src.endpoints.index import Index
from .src.endpoints.menu import Menu
from .src.endpoints.posts import Posts, api as posts
from .src.endpoints.addresses import Addresses, api as addr

app = Flask(__name__, static_url_path='',
            static_folder=Constants.STATIC_FOLDER)
api = Api(app, no_doc=True)
session = {}

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(asctime)s - '
                    '%(filename)s:%(lineno)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

api.add_namespace(login)
api.add_namespace(posts)
api.add_namespace(addr)

api.add_resource(Index, "/")
api.add_resource(Menu, "/main_menu")
login.add_resource(GoogleLogIn, "/login", resource_class_kwargs={})
login.add_resource(LogInSuccessPage, "/loggedin")
# login.add_resource(VerifyUserLogin, "/callback")
posts.add_resource(Posts, "/posts")
addr.add_resource(Addresses, "/addr")

if __name__ == "__main__":
    app.run(debug=True)
