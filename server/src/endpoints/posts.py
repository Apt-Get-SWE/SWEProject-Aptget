from flask_restful import Resource
from ..types.post import Post
from ..types.utils import parse_json

class Posts(Resource):
    def get(self):
        data = parse_json(Post.find_all())
        formatted_data = {}
        for post in data:
            formatted_data[post['pid']] = post

        return {
            'Type' : 'Data',
            'Title' : 'List of posts',
            'Data' : formatted_data
        }