from flask_restx import Resource
from flask import send_from_directory
from ..constants import Constants

class Index(Resource):
    def get(self):
        return send_from_directory(Constants.STATIC_FOLDER, 'index.html')