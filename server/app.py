# -----------------------------------------------------------------------------
# AptGet API
# -----------------------------------------------------------------------------
# This is the file containing all of the endpoints for our Flask app.
# The endpoint called `endpoints` will return all available endpoints.
# -----------------------------------------------------------------------------

# Importing required libraries and modules
from flask import Flask, Blueprint
from flask_restx import Api
import logging
from .src.endpoints.login import GoogleLogIn, RestrictedArea, SaveUserLogin, LogOut, api as login
from .src.constants import Constants
from .src.endpoints.menu import Menu
from .src.endpoints.posts import Posts, MarketPosts, api as posts
from .src.endpoints.users import Users, GetUserAddress, LinkUserAddress, api as users
from .src.endpoints.addresses import Addresses, api as addr

# Initializing Flask app and Blueprint
app = Flask(__name__, static_folder=Constants.STATIC_FOLDER)
blueprint = Blueprint('api', __name__, url_prefix='/api')

# Initializing Api with the Flask app and Blueprint
api = Api(blueprint,
          title='AptGet API',
          version='v0.1',
          doc='/docs',
          base_url='/api'
          )

# Registering Blueprint with the app
app.register_blueprint(blueprint)

# Adding a secret key for session support
app.secret_key = "some_random_key"  # TODO: make this a env variable

# Setting up logging
logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(asctime)s - '
                    '%(filename)s:%(lineno)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# Adding namespaces to the API
api.add_namespace(login)
api.add_namespace(posts)
api.add_namespace(users)
api.add_namespace(addr)

# Adding resources to the namespaces
api.add_resource(Menu, "/main_menu")
login.add_resource(GoogleLogIn, "/login", resource_class_kwargs={})
login.add_resource(RestrictedArea, "/restricted_area", resource_class_kwargs={})
login.add_resource(SaveUserLogin, "/callback")
login.add_resource(LogOut, "/logout")
posts.add_resource(Posts, "/posts")
posts.add_resource(MarketPosts, "/market_posts")
users.add_resource(Users, "/users")
users.add_resource(GetUserAddress, "/get_user_address")
users.add_resource(LinkUserAddress, "/link")
addr.add_resource(Addresses, "/addr")


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
